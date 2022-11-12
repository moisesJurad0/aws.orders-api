import os

import boto3
import simplejson as json  # import json
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    print('event->')
    print(event)

    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get('ORDERS_TABLE')
    table = dynamodb.Table(table_name)
    order_id = int(event['pathParameters']['id'])
    response = table.query(
        KeyConditionExpression=Key('id').eq(order_id)
    )

    print('response->')
    print(response)

    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps(response['Items'])
    }
