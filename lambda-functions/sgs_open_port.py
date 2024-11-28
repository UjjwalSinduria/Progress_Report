import boto3
import json
ec2_client = boto3.client('ec2')
s3_client = boto3.client('s3')
def lambda_handler(event,context):
    bucket_name = "amit-s3demo"
    s3_path = "open_port.csv"
    response = ec2_client.describe_security_groups()
    ans = []
    
    for port in response.get("SecurityGroups",[]):
        if len(port['IpPermissions']) != 0:
            if port['IpPermissions'][0].get("IpRanges",[]) != [] :
                if port['IpPermissions'][0].get("IpRanges",[])[0].get('CidrIp') == "0.0.0.0/0":
                    ans.append(f'Gropu_Id:{port["GroupId"]} -------'+port['IpPermissions'][0].get("IpRanges",[])[0].get('CidrIp'))

    s3_client.put_object(
        Key=s3_path,
        Bucket=bucket_name,
        Body=(json.dumps(ans))
    )


