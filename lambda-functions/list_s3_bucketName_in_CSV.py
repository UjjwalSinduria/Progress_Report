import boto3

client = boto3.client('s3')

def lambda_handler(event,context):
    result = []
    response = client.list_buckets()
    for res in response['Buckets']:
        result.append(res['Name'])
    print(result[0])
    # amit-s3demo
    bucket_name = "amit-s3demo"
    file_name="list_content.csv"
   
   

    client.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=','.join(result)
    )






    
