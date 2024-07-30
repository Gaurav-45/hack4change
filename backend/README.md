# The backend APIs in Flask 

Environment File Setup 

Name the file as .env and add the below code - 

```
CROP_PREDICTOR_API_KEY = "YOUR API KEY"
GROQ_API_KEY = "YOUR API KEY"
```


1) getCropPrice 

API URL - http://localhost:5000/getCropPrice

Expected JSON Request Payload in body - 
```
{
    "state": "Telangana",
    "district": "Khammam",
    "commodity": "Banana"
}

```

Response - 

```

{
    "message": "Success",
    "metaData": {
        "state": "Telangana",
        "district": "Khammam",
        "commodity": "Banana"
    },
    "result": [
        {
            "State": "Telangana",
            "District": "Khammam",
            "Market": "Sattupalli",
            "Commodity": "Banana",
            "Variety": "Other",
            "Grade": "FAQ",
            "Arrival_Date": "14/09/2012",
            "Min_Price": "1700",
            "Max_Price": "1750",
            "Modal_Price": "1730",
            "Commodity_Code": "19"
        },
        {
            "State": "Telangana",
            "District": "Khammam",
            "Market": "Sattupalli",
            "Commodity": "Banana",
            "Variety": "Other",
            "Grade": "FAQ",
            "Arrival_Date": "21/09/2012",
            "Min_Price": "400",
            "Max_Price": "430",
            "Modal_Price": "400",
            "Commodity_Code": "19"
        },
        {
            "State": "Telangana",
            "District": "Khammam",
            "Market": "Dammapet",
            "Commodity": "Banana",
            "Variety": "Other",
            "Grade": "Medium",
            "Arrival_Date": "21/07/2015",
            "Min_Price": "400",
            "Max_Price": "400",
            "Modal_Price": "400",
            "Commodity_Code": "19"
        },
        {
            "State": "Telangana",
            "District": "Khammam",
            "Market": "Dammapet",
            "Commodity": "Banana",
            "Variety": "Other",
            "Grade": "Medium",
            "Arrival_Date": "03/08/2015",
            "Min_Price": "400",
            "Max_Price": "400",
            "Modal_Price": "400",
            "Commodity_Code": "19"
        },
        {
            "State": "Telangana",
            "District": "Khammam",
            "Market": "Dammapet",
            "Commodity": "Banana",
            "Variety": "Other",
            "Grade": "Medium",
            "Arrival_Date": "05/08/2015",
            "Min_Price": "400",
            "Max_Price": "400",
            "Modal_Price": "400",
            "Commodity_Code": "19"
        },
        {
            "State": "Telangana",
            "District": "Khammam",
            "Market": "Dammapet",
            "Commodity": "Banana",
            "Variety": "Other",
            "Grade": "Medium",
            "Arrival_Date": "19/08/2015",
            "Min_Price": "400",
            "Max_Price": "400",
            "Modal_Price": "400",
            "Commodity_Code": "19"
        },
        {
            "State": "Telangana",
            "District": "Khammam",
            "Market": "Dammapet",
            "Commodity": "Banana",
            "Variety": "Other",
            "Grade": "Medium",
            "Arrival_Date": "23/08/2015",
            "Min_Price": "400",
            "Max_Price": "400",
            "Modal_Price": "400",
            "Commodity_Code": "19"
        },
        {
            "State": "Telangana",
            "District": "Khammam",
            "Market": "Dammapet",
            "Commodity": "Banana",
            "Variety": "Other",
            "Grade": "Medium",
            "Arrival_Date": "31/08/2015",
            "Min_Price": "400",
            "Max_Price": "400",
            "Modal_Price": "400",
            "Commodity_Code": "19"
        },
        {
            "State": "Telangana",
            "District": "Khammam",
            "Market": "Dammapet",
            "Commodity": "Banana",
            "Variety": "Other",
            "Grade": "Medium",
            "Arrival_Date": "03/09/2015",
            "Min_Price": "1380",
            "Max_Price": "1400",
            "Modal_Price": "1390",
            "Commodity_Code": "19"
        },
        {
            "State": "Telangana",
            "District": "Khammam",
            "Market": "Dammapet",
            "Commodity": "Banana",
            "Variety": "Other",
            "Grade": "Large",
            "Arrival_Date": "22/09/2015",
            "Min_Price": "400",
            "Max_Price": "400",
            "Modal_Price": "400",
            "Commodity_Code": "19"
        }
    ]
}

```


2) getCropDiseaseInformation -  API to generate Disease Information 

API URL - http://localhost:5000/getCropDiseaseInformation

Expected JSON Request Payload in body -

```
{
    "disease": "Bacterial Leaf Spot"
}
```

Response -
```
{
    "message": "Success",
    "metaData": {
        "disease": "Bacterial Leaf Spot"
    },
    "result": {
        "information": "Bacterial Leaf Spot is a common disease affecting various crops, including tomatoes, peppers, and cucumbers. It is caused by the bacterium Xanthomonas campestris.",
        "causes": "The disease is spread through contaminated water, infected seeds, and contact with infected plants. It thrives in warm and humid environments.",
        "treatment": "Early detection and removal of infected plants are crucial. Chemical control involves applying copper-based fungicides, while biological control involves using beneficial bacteria to outcompete the pathogen.",
        "medicine": [
            {
                "name": "Copper-based fungicide",
                "information": "Apply 1-2% copper oxychloride solution to the affected area."
            },
            {
                "name": "Beneficial bacteria",
                "information": "Apply Bacillus subtilis or Pseudomonas fluorescens to the soil to outcompete the pathogen."
            }
        ]
    }
}

```