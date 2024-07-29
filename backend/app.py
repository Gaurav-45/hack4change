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

        if(data["filters[state.keyword]"]):
            params["filters[state.keyword]"] = data['state']
        
        if(data["filters[district]"]):
            params["filters[district]"] =  data['district']
        
        if(data["filters[commodity]"]):
            params["filters[commodity]"] = data['commodity']
        
            
        res = requests.get("https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070", params)

        response_bytes = res.content
        responseData = json.loads(response_bytes.decode('utf-8'))  # Assuming UTF-8 encoding

        print("response - ", responseData)

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