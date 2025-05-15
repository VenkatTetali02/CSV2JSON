import json
import boto3
import botocore.config

def generate_json_from_csv(lst):

    query=f"""You are an expert reader in reading a array list of CSV strings.Dont provide any other supplemental information.
           Below are the few examples on how the information appears and how it should be extracted in JSON format
           
           Example1:
           {{"input":["012636633","Test Name1","Computer Science","3.7","Advisor Name1",";","733939","Test Name2","Bachelors in History","3.2","Advisor Name2"]}}
           
           [
            {{'StudentId':'012636633','Name':'Test Name1','Major':'Computer Science','GPA':'3.7','Advisor':'Advisor Name1'}},
            {{'StudentId':"733939",'Name':'Test Name2','Major':'Bachelors in History','GPA':'3.2','Advisor':'Advisor Name2'}}
           ]

           Example2: 
            {{"input":["123232","Test Name7","Bachelor in Economics","3.4","Advisor Name10"]}}
             "output_text":[
            {{'StudentId':"123232",'Name':'Test Name7','Major':'Bachelor in Economics','GPA':'3.4','Advisor':'Advisor Name10'}}
           ]

           Now generate for
           {lst}\n
         
           """
    body={
            "inputText":query,
            "textGenerationConfig":{
                "maxTokenCount":4096,
                "temperature":0
            }
        }
    
    bedrock=boto3.client("bedrock-runtime",region_name='us-east-1',
                                 config=botocore.config.Config(read_timeout=300,retries={'max_attempts':3}))
    
    response=bedrock.invoke_model(modelId='amazon.titan-text-lite-v1',
        contentType='application/json',
        accept="application/json",
        body=json.dumps(body))
    
    json_data=json.loads(response['body'].read().decode('utf-8'))


    json_results=json_data["results"]

    # print(json_results)
    
    print(json_results[0]['outputText'])
  
test={"input":["0126333333","Test Name1","Computer Science","8.7","Advisor Name1","\n","733977539","Test Name2","Bachelors in History","3.2","Advisor Name2","\n","123456","Test Name2","MS in CS","4.2","Advisor Name3"]}
generate_json_from_csv(test)

