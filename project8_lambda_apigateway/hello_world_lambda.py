def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': '{"message": "Hello, world! This is a Lambda function exposed via API Gateway."}'
    } 