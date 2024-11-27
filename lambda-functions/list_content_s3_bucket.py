import boto3

s3 = boto3.client('s3')
def lambda_handler(event, context):
    try:
        response = s3.list_objects_v2(Bucket = s3.list_buckets()['Buckets'][0]['Name'])
        for content in response["Contents"]:
            print(content['Key'])
    except:
        return{
            'statusCode':500,
            'body':'Response not found'
            }
        

   