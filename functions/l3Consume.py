import json


def handler(event, context):
    message_from_publisher = json.loads(event['Records'][0]['Sns']['Message'])
    my_param = message_from_publisher['myParamFromConsumerPublisher']
    print("👷 Received paramater from ConsumerPublisher: '{0}'".format(my_param))
    
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

