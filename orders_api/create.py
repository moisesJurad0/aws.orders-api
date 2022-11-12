import json
import app

def lambda_handler(event, context):
    print('event->')
    print(event)

    dynamodb = app.dynamodb
    table_name = app.table_name

    order = json.loads(event['body'])
    table = dynamodb.Table(table_name)
    response = table.put_item(TableName=table_name, Item=order)

    print('response->')
    print(response)

    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'message': 'Order Created'})
    }
