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
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

from helpers.twiliohelper import makeCall, makeSMS

load_dotenv()
app = Flask(__name__)
CORS(app)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def query_documents_local(collection, question):
    results = collection.similarity_search_with_score(query=question, k=1)
    return results


def chroma_init():
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    persist_directory = "./db"
    if not os.path.exists(persist_directory):
        os.makedirs(persist_directory)

    collection = Chroma(
        collection_name="farmer-schemes-govi",
        embedding_function=embedding_function,
        persist_directory=persist_directory,
    )

    return collection

class Medicine(BaseModel):
    name: str
    information: str
    dose: str

class CropDisease(BaseModel):
    information: str
    causes: str
    treatment: str
    medicine: List[Medicine]

@app.route("/getCropPrice", methods=["GET", "POST"])
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
        print("responseData : ", responseData)
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
       print("Exception -- ", str(ex))
       return {"error": str(ex)}, 500

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
    

@app.route("/api/chat", methods=["POST"])
def chat_response():
    try:
        request_data = request.get_json()

        # Extract the user message
        messages = request_data.get("messages", [])
        user_message = ""

        if (
            messages
            and "text" in messages[0]
            and (messages[0]["text"] != "Yes" and messages[0]["text"] != "No")
        ):
            user_message = messages[0]["text"]
            query = user_message
            collection = chroma_init()
            resp = query_documents_local(collection, query)
            final_resp = f"title - {resp[0][0].metadata['title']}, content - {resp[0][0].page_content}"

            print("Context - ",final_resp)

            print("final conetne  - ",f"Consider you are a farmer assistant that has to answer the questions of the farmers based on context provided. Consider this context - {final_resp}\n")
            
            chat_completion = client.chat.completions.create(messages=[
                    {
                        "role": "system", 
                        "content": f"Consider you are a farmer assistant that has to answer the questions of the farmers based on context provided. Summarize the answer to include only certain important points in a proper format. Also consider that this information is being displayed to a farmer who does not have a lot of technical knowledge about finance and all so make the content easy to understand and how will it be able to help the farmer in what way.Generate the response in hindi. Consider this context - {final_resp}\n"
                    },
                    {
                        "role": "user",
                        "content": query
                    }
                ],
                model="llama3-8b-8192",
                temperature=0,
                stream=False
            )

            print("respopppp - ",chat_completion.choices[0])
            response = chat_completion.choices[0].message.content
            response_data = {
                "role": "ai",
                "text": response,
            }

            print()
            print()
            print("finallllllllllllll - ",response_data)

            return [response_data]
        else:
            response_data = {
                "role": "ai",
                "text": f"Thanks recorded!",
            }
            return [response_data]
    except Exception as ex:
        print("Exception --", ex)
    

api = Api(app)

if __name__ == '__main__':
  print("Server running succesfully")
  app.run(debug="True")