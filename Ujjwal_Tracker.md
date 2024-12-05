### Monday 18-11-2024

- [x] IAM,AMI, ec2, Container services
- [x] Servless, Fargate, Lambda
- [x] Networking, Amazon VPC

### Tuesday 19-11-2024

- [x] Amazon VPC, Internet Gateway, Virtual Private Gateway
- [x] Amazon VPC Routing, Route Table, Main Route Table , Custom Route Table, Subnet Route Table
- [x] Amazon VPC Security, Access Control List, Secure Ec2 instance with Security Groups
- [x] AWS Networking Basics, Network Foundation, Hybrid Connectivity, Edge networking, Application Networking, Network Security
- [x] IPV4, IPV6, CIDR, Subnetting, Subnet mask

### Wednesday 20-11-2024

- [x] Storage, File Storage, Block Storage, Object Storage
- [x] Amazon EFS, Amazon ec2 Instance Store, Amazon EBS, EBS Volume types(SSDs, HDDs)
- [x] Understanding the Structure of IPs, Addressing, IPV4, IPV4 classes, IPV6, Public IP, Private IP
- [x] \*\*\*Task1: Created first Amazon Ec2 instance using Management Console

### Thursday 21-11-2024

- [x] Amazon EBS Snapshots, Amazon S3, S3 Storage Classes, Amazon S3 bucket policies, Amazon S3 Encryption
- [x] Monitoring, Amazon S3 Matrics, Amazon RDS Matrics, Amazon ec2 Matrics
- [x] Amazon CloudWatch, CloudWatch DashBoards, Amazon CloudWatch Logs, CloudWatch Alarms
- [x] Ok State, Alarm State, Insufficient Data

### Friday 22-11-2024

- [x] Traffic Routing, Elastic Load Balancing, Application Load Balancer, Network Load Balancer, Gateway Load Balancer
- [x] Amazon ec2 Auto Scaling, Traditional Scaling VS Auto Scaling, Automatic Scaling, Scheduled Scaling, Predicitive Scaling
- [x] ELB with Amazon ec2 Auto Scaling, Amazon ec2 Autoscaling groups (Minimun, Desired and Maximum Capicity)
- [x] ec2 Autoscaling Policies (Dynamic Policies, Predicitive polices, Scheduled Policies), How the policy works
- [x] \*\*\*Task2: Created an ec2 instance and hosted it on apache server
- [x] \*\*\*Task3: Created 2 ec2 instance and observed the changes using bootstrap code for apache

### Monday 25-11-2024

- [x] \*\*\*Task4: Created a Load Balancer for ec2 and distributed it among them and test in the browser
- [x] \*\*\*Task5: Created a AutoScaling group for ec2 instance.
- [x] \*\*\*Task6: Apache on EC2 and Put EC2 in an ASG with ELB.
- [x] \*\*\*Task6: Basics linux Commands

### Tuesday 26-11-2024

- [x] \*\*\*Task7: Create an IAM role with access to S3 services, use AWS CLI from instance to list bucket in s3
- [x] \*\*\*Task8: Create VPC with custom IGW and created public and private subnets with different public and private route tables
- [x] \*\*\*Task8: Create VPC endpoint to S3

### Wednesday 27-11-2024

- [x] \*\*\*Task8: continued with the task8(able to access private instance, but with some unresolved doubts(why private instance getting the internet access without NAT gateway))
- [x] AWS lambda :
- [x] \*\*\*Task9: List all S3 buckets using AWS Lambda.
- [x] \*\*\*Task10: List the contents of a S3 bucket. (Any bucket)
- [x] \*\*\*Task11: Get the names of each object of the S3 bucket and put in a file in a csv format and put it in a bucket(Not completed)

### Thursday 28-11-2024

- [x] \*\*\*Task11: Get the names of each object of the S3 bucket and put in a file in a csv format and put it in a bucket
- [x] \*\*\*Task12: Get the list of all Security Groups inside all the VPCs. Take a VPC that has maximum number SGs.
- [x] \*\*\*Task13: Put the names of the SGs that have any port open to 0.0.0.0 in a file.
- [x] What is EventBridge, EventBuses, Pipes

### Friday 29-11-2024

- [x] \*\*\*Task14: Utilise Event bridge as a trigger for the previous lambda functions.
- [x] \*\*\*Task15: Create a bucket and 2 folders.
- [x] \*\*\*Task16: Upload files to these folders using CLI and console.
- [x] \*\*\*Task17: Configure the bucket to host static website and host sample html page.
- [x] \*\*\*Task18: Read about different tiers of S3.
- [x] \*\*\*Task19: Read about bucket policies.


### Monday 02-12-2024
- [x] \*\*\*Task20: Spin up an EC2 Instance with Security Group. EC2 instance should have a Tag with you name
- [x] \*\*\*Task21: Tag resources Tag 5 resources: EC2, AWS Lambda ,S3 Bucket ,VPCs  
    (Query: Can't find the perfect function to add new tag to the s3 bucket without deleting previous one
    * put_bucket_tagging(It will delete previous tags and then add new tags)
    * new Approach: get_bucket_tagging(With the help of this retrieve old tags and append new tag into that tag list)
      BucketTagging.put(With the help of this add all old+newTag into the bucket)
    )


### Tuesday 03-12-2024
- [x] \*\*\*Task21(Continue): (Found another method, which can add new tags in multiple resources at once())(But it requires ARNs to perform the task )
- [x] \*\*\*Task22: Created a another lambda function to remove all the selected tags from all the given resources
- [x] \*\*\*Task23: Create CloudWatch alarm for a EC2 instance, and create alarms on metrics:  
    * CPU Utilization  
    * Memory Usage Percentage  


### Wednesday 04-12-2024
- [x] \*\*\*Task24: With the help of cft i have created sg, ec2, CpuUtilization Alarm, Memory Usage Percentage
- [x] \*\*\*Task25: API Gateway Trigger for your AWS Lambda Function for the Lambda function for task 21&22. Then, based on the POST payload, the Lambda function will  tag the resource. For example, if the payload has EC2, then EC2 will be tagged. Similarly, if the request is to remove the Tag, then remove the tag for the appropriate resource/service. (Now, any test case or scenario that should be considered, should be handled.) 


### Thursday 05-12-2024
- [x] \*\*\*Task26: CloudFormation template for task(24 and 25).
- [x] \*\*\*Task27: VPC Three tier architecture
      * Revised about Internet Gateway,Virtual Private Gateway, Route Tables, Subnets

 

            
            



