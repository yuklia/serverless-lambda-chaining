import json, boto3, os


def handler(event, context):
    message_from_publisher = json.loads(event['Records'][0]['Sns']['Message'])
    my_param = message_from_publisher['myParamFromPublisher']
    print("👷 Received paramater from publisher: '{0}'".format(my_param))
    client = boto3.client('sns')

    # Message attributes are sent only when the message structure is String, not JSON
    snsResponse= client.publish(
        TopicArn=os.environ['snsTopicForConsumer2Arn'],
        Message=json.dumps({"default": json.dumps({'myParamFromConsumerPublisher': my_param})}),
        Subject='TestConsumerPublisher',
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