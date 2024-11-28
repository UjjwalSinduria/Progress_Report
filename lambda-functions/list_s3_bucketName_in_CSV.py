# amit-s3demo
import boto3
import csv
import io
region = "us-east-1" 
s3 = boto3.client('s3',region_name=region)
def lambda_handler(event, context):
    try:
        result = []
        response = s3.list_buckets()
        s3.create_bucket(Bucket='ujjwal-test-bucket',CreateBucketConfiguration={'LocationConstraint': region})
        print(f'bucket ujjwal-test-bucket is created in {region} region')
        for bucket in response['Buckets']:
            result.append(bucket['Name'])
        csv_buffer = io.StringIO()
        csv_writer = csv.writer(csv_buffer)
        csv_writer.writerows(result)
        csv_content = csv_buffer.getvalue()
        s3.put_object(
            Bucket='ujjwal-test-bucket',
            Key='list_fileName.csv',
            Body=csv_content,
            ContentType='text/csv'
        )
        
        
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

    )


    


        
        
    except:
        print('Not working')