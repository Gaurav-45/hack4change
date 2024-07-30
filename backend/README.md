# The backend APIs in Flask 

Environment File Setup 

Name the file as .env and add the below code - 

```
CROP_PREDICTOR_API_KEY = "YOUR API KEY"
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