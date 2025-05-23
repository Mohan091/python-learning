import boto3 
from boto3 import *
import os


AWS_ACCESS_KEY_ID = "AKIA2OAJTNWOH3HITSH5"
AWS_SECRET_ACCESS_KEY = "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"
REGION_NAME = "us-east-1"
BUCKET_NAME = "test_bucket"

aws_console = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY,region_name=REGION_NAME)

print(aws_console)
# print(aws_console.get_available_resources())

iam_client = boto3.client('iam')
s3_client = boto3.client('s3')
my_bucket = s3_client.create_bucket(Bucket=BUCKET_NAME)
# print(my_bucket)

bucket_object = s3_client.list_objects_v2(Bucket=BUCKET_NAME)

print(bucket_object)
# for each in iam_client.list_users()['Users']:
#     print(each['UserName'])

# for each in s3_client.list_buckets()['Buckets']:
#     print(each['Name'])    

# for each_bucket in s3_client.list_buckets():
#     print(each_bucket.Name)    