import json, boto3, os


def handler(event, context):
    my_param = event['pathParameters']['myParam']
    print("Query paramater: '{0}'".format(my_param))
    client = boto3.client('sns')

    # Message attributes are sent only when the message structure is String, not JSON
    snsResponse= client.publish(
        TopicArn=os.environ['snsTopicForConsumer1Arn'],
        Message=json.dumps({"default": json.dumps({'myParamFromPublisher': my_param})}),
        Subject='Test',
        MessageStructure='json',
        MessageAttributes={
            'test-attr': {
                'DataType': 'String',
                'StringValue': 'myAttrValue'
            }
        }
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(snsResponse)
    }

    return response

