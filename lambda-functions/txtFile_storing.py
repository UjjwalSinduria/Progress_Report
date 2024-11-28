import json
import boto3
s3_client = boto3.client('s3')
def lambda_handler(event,context):
    bucket_name = "amit-s3demo"
    s3_path_001 = "001"
    list_file = ['hi','this','is','first bucket']
    s3_client.put_object(
        Key=s3_path_001,
        Bucket=bucket_name,
        Body=(json.dumpsS(list_file))
    )