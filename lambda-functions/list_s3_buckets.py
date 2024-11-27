import boto3


client = boto3.client('s3')
def lambda_handler(event,context):
    response = client.list_buckets()
    try:
        for bucket in response['Buckets']:
            print(bucket['Name'])
    except:
        print('NO response found')