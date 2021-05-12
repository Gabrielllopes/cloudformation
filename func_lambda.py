# biblioteca para manipular serviços aws
import boto3
import uuid
import json
from decimal import Decimal

def lambda_handler(event, contex):
    
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("orders")

    # pegando mensagem 
    body = json.loads(event["Records"][0]["body"])
    message = json.loads(body["Message"], parse_float=Decimal)


    table.put_item(
        Item = {
            "id": str(uuid.uuid4()),
            "content": message
        }
    )