# CSV2JSON Converter

LLM based project which converts the list of CSV strings separted by new line character into JSON which then can be consumed by donwstream processes.
Created API Gateway which provides us the endpoint through which we can trigger our Lambda function.
We use the Titan model provided by the AWS Bedrock to generate the JSON content.

## Techstack
- AWS API Gateway
- AWS Lambda
- AWS Bedrock (Titan Model)

## Usage
``` 
curl --location 'https://sampleapi.execute-api.us-east-1.amazonaws.com/dev/csv2json' \
--header 'Content-Type: application/json' \
--data '{
    "input": [
        "0126333333",
        "John Mathew",
        "Computer Science",
        "3.5",
        "Advisor Name1",
        "\n",
        "733977539",
        "William",
        "Bachelors in History",
        "3.6",
        "Advisor Name2",
        "\n",
        "123456",
        "Rachel",
        "MS in CS",
        "4.7",
        "Advisor Name3"
    ]
}'
```

