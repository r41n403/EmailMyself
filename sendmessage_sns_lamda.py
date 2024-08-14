import json
import boto3
import os

def lambda_handler(event, context):
    # Initialize SNS client
    sns_client = boto3.client('sns')
    
    # Extract the SNS Topic ARN from environment variables
    sns_topic_arn = os.environ['SNS_TOPIC_ARN']
    
    try:
        # Parse the incoming JSON data
        body = json.loads(event['body'])
        
        # Publish the message to the SNS topic
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=json.dumps(body),
            Subject='New Message from Lambda'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Message published successfully',
                'messageId': response['MessageId']
            })
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
