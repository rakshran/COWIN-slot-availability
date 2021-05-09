import http.client
import json
import boto3
from datetime import date
import datetime

today = str(date.today())
today = datetime.datetime.strptime(today, "%Y-%m-%d").strftime("%d-%m-%Y")


def lambda_handler(event, context):
    client = boto3.client('sns')
    conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
    payload = ''
    headers = {}
    url = '/api/v2/appointment/sessions/public/calendarByDistrict?district_id=YOUR_DISTRICT_ID&date='+str(today)
    print(url)
    conn.request("GET", url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    
    vaccine = json.loads(data.decode("utf-8"))
    final_response = ''

        
    for item in vaccine["centers"]:
        for session in item["sessions"]:
            if session["min_age_limit"] == 18 and session["available_capacity"] > 0:
            #if session["min_age_limit"] == 18:
                data_to_return =  item["name"] + ' - ' + item["address"] + ' - ' + str(item["pincode"]) + ' - ' + session["date"] + ' - ' + str(session["available_capacity"])
                final_response = final_response + "\n" + data_to_return
                response = client.publish(
                TopicArn=YOUR_SNS_TOPIC_ARN, Message= final_response, Subject='Vaccine slots opened')
            else:
                exit()
    
    return response     



