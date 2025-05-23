import boto3
import boto3.session 
import os 
import requests

# import data

ACCESS_KEY_ID = 'AKIA2OAJTNWOH3HITSH5'
SECRET_ACCESS_KEY = '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'
REGION_NAME = 'ap-northeast-1'
PROFILE_NAME = 'dev'

aws_console = boto3.session.Session(
      aws_access_key_id=ACCESS_KEY_ID,aws_secret_access_key=SECRET_ACCESS_KEY,
      region_name=REGION_NAME)


# session = Session(profile_name=PROFILE_NAME,
#     aws_access_key_id=ACCESS_KEY_ID,
#     aws_secret_access_key=SECRET_ACCESS_KEY,
#     region_name=REGION_NAME
# )

print(aws_console)
# print(dir(aws_console))

# print(aws_console.get_available_resources())

# print(aws_console.get_available_services())



s3_resource = aws_console.resource('s3')
iam_resource = aws_console.resource('iam')
s3_client = aws_console.client('s3')
iam_client = aws_console.client('iam')
ec2_client = aws_console.client('ec2')

bucket_name = 'boto30-test-bucket'
my_bucket = s3_resource.Bucket(bucket_name)


for files in my_bucket.objects.all():
  print(files.key)

# # print(os.getcwd())
 
# print("before uplaod")
# upload_file = '/home/runner/modules/testfile.txt'
# my_bucket.upload_file(upload_file, 'testfile.txt')

# print(f"upload file {upload_file} in {bucket_name}")



# for user_list in iam_resource.users.all():
#   print(user_list.name)

# for each in s3_client.list_buckets()['Buckets']:
#   print(each['Name'])


# for each in iam_client.list_users()['Users']:
#   print(each['UserName'])



# for reservation in ec2_client.describe_instances()['Reservations']:
#   for instance in reservation['Instances']:
#     print(instance['InstanceId'])



# ec2_create_instance = ec2_client.run_instances(
#     ImageId = 'ami-0b2cd2a95639e0e5b',
#     InstanceType = 't2.micro',
#     KeyName = 'suryakey',
#     MinCount = 1,
#     MaxCount = 1
# )

# ec2_terminate_instance = ec2_client.stop_instances( InstanceIds = ["i-070ca28a7a7c350d5"]
# )

# ec2_terminate_instance = ec2_client.terminate_instances( InstanceIds = ["i-070ca28a7a7c350d5"]
# )


