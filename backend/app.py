from flask import Flask, Response, request
from flask_restful import Api, Resource
from flask import request
from flask_cors import CORS
from dotenv import load_dotenv
import json
import requests
import os
from groq import Groq
from pydantic import BaseModel
from typing import List

from helpers.twiliohelper import makeCall, makeSMS

load_dotenv()
app = Flask(__name__)
CORS(app)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

class Medicine(BaseModel):
    name: str
    information: str
    dose: str

class CropDisease(BaseModel):
    information: str
    causes: str
    treatment: str
    medicine: List[Medicine]

@app.route("/getCropPrice", methods=["GET"])
def getCropPrice():
    try:
        print("request Payload - ", json.loads(request.data))
        data = json.loads(request.data)

        params = {
           "api-key":  os.environ.get('CROP_PREDICTOR_API_KEY'),
           "format": 'json',
           "offset":0,
           "limit":10,
        }

        if "state" in data:
            params["filters[state.keyword]"] = data["state"]

        if "district" in data:
            params["filters[district]"] =  data["district"]
        
        
        if "commodity" in data:
            params["filters[commodity]"] = data["commodity"]
        

        print("Params - ", params)
            
        res = requests.get("https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070", params)

        response_bytes = res.content
        responseData = json.loads(response_bytes.decode('utf-8'))  # Assuming UTF-8 encoding

        print("response - ", responseData["records"])

        return Response(
           response=json.dumps({
            "message":"Success",
            "metaData": data,
            "result": responseData["records"]
            }),
           status = 200,
           mimetype="application/json"

        )
        
    except Exception as ex:
       print("Exception -- ", ex)

@app.route("/getCropDiseaseInformation", methods=["GET", "POST"])
def getCropDiseaseInformation():
    try:
        print("request Payload - ", json.loads(request.data))
        data = json.loads(request.data)
        if "disease" not in data:
            raise Exception("Disease name is required")
        chat_completion = client.chat.completions.create(messages=[
             {
                "role": "system", 
                "content": "You are a farmer assistant that outputs responses in JSON.\n"
                # Pass the json schema to the model. Pretty printing improves results.
                f" The JSON object must use the schema: {json.dumps(CropDisease.model_json_schema(), indent=2)}",
            },
            {
                "role": "user",
                # - { information: string , causes: string ,treatment: string , medicine: string}
                "content": "Give accurate information for the following crop disease - " + str(data["disease"]) + ". Also provide its causes, treatment and medicine dosage to use. Provide the response strictly in expected JSON format with the mentioned datatype."
            }
        ],
        model="llama3-8b-8192",
        temperature=0,
        stream=False,
        response_format={"type": "json_object"},
        )

        print(chat_completion.choices[0].message.content)

        response = chat_completion.choices[0].message.content
        
        return Response(
           response=json.dumps({
            "message":"Success",
            "metaData": data,
            "result": json.loads(response),
            }),
           status = 200,
           mimetype="application/json"

        )

    except Exception as ex:
        print("Exception --", ex)

@app.route("/call-sms", methods=["GET", "POST"])
def fun_call_sms():
    try:
        # phone_number = request.json['phone_number']
        phone_number = '+91XXXXXXXXXX'
        message = """किसान मित्रों,
        
        कृपया ध्यान दें, कुछ ही घंटों में मौसम बदलने की संभावना है। कृपया अपनी फसलों की सुरक्षा के लिए आवश्यक कदम उठाएं।

        धन्यवाद,
        आपका कृषि बंधु ऐप
        """
        makeCall(phone_number, message)
        makeSMS(phone_number, message)
        return {"data": "success"}, 200
    except Exception as ex:
        print(f"--error: {str(ex)}")
        return {"error": str(ex)}, 500

api = Api(app)

if __name__ == '__main__':
  print("Server running succesfully")
  app.run(debug="True")