import json
from datetime import datetime

def lambda_handler(event, context):
    path = event.get("rawPath")

    if path == "/hello":
        name = "Guest"
        if event.get("queryStringParameters"):
            name = event["queryStringParameters"].get("name", "Guest")

        return {
            'statusCode': 200,
            'body': json.dumps(f"Hello, {name}")
        }

    elif path == "/time":
        return {
            'statusCode': 200,
            'body': json.dumps(f"Current time: {datetime.now()}")
        }

    else:
        return {
            'statusCode': 404,
            'body': json.dumps("Route not found")
        }