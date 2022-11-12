import simplejson as json  # import json
from boto3.dynamodb.conditions import Key

import app


def lambda_handler(event, context):
    print('event->')
    print(event)

    dynamodb = app.dynamodb
    table_name = app.table_name

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
