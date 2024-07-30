from flask import Flask, Response, request
from flask_restful import Api, Resource
from flask import request
from flask_cors import CORS
from dotenv import load_dotenv
import json
import requests
import os

load_dotenv()
app = Flask(__name__)
CORS(app)


@app.route("/getCropPrice", methods=["GET"])
def getCropPrice():
    try:
        print("request Payload - ", json.loads(request.data))
        data = json.loads(request.data)

        params = {
           "api-key":  os.environ.get('API_KEY'),
           "format": 'json',
           "offset":0,
           "limit":10,
        }

        if "state" in data:
            params["filters[State.keyword]"] = data["state"]
        
        if "district" in data:
            params["filters[District.keyword]"] =  data["district"]
        
        if "commodity" in data:
            params["filters[Commodity.keyword]"] = data["commodity"]
        

        print("Params - ", params)
            
        res = requests.get("https://api.data.gov.in/resource/35985678-0d79-46b4-9ed6-6f13308a1d24", params)

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



api = Api(app)

if __name__ == '__main__':
  print("Server running succesfully")
  app.run(debug="True")