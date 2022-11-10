import json


def lambda_handler(event, context):
    order = {'id': 123, 'itemName': 'Mac Book Pro', 'Quantity': 100}
    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps(order)
    }
