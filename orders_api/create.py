import json
import os

import boto3


def lambda_handler(event, context):
    print('event->')
    print(event)

    order = json.loads(event['body'])
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get('ORDERS_TABLE')
    table = dynamodb.Table(table_name)
    response = table.put_item(TableName=table_name, Item=order)
    print('response->')
    print(response)
    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'message': 'Order Created'})
    }
