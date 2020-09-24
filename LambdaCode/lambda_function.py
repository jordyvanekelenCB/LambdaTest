import json

print('Loading function...')

print('I exisddsssssst!')

def lambda_handler(event, context):
    """
    print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key2'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    """

    body = {
        "president": {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
        }
    }

    return {
        "statusCode": 200,
        'headers': { 'Content-Type': 'application/json' },
        "body": json.dumps(body)
    }

    # return '{"key": "val"}'
    # return event['key1']  # Echo back the first key value
    # raise Exception('Something went wrong')
