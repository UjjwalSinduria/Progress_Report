import boto3
import csv
from io import StringIO

def lambda_handler(event,context):
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    result = []
    for res in response['Buckets']:
        result.append(res['Name'])
        
    print(result)