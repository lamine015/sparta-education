import boto3
import pprint as pp

region = "eu-west-1"
#s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3', region_name=region)
bucket_name = "se-mohamed-bucket"

all_buckets = [bucket.name for bucket in s3_resource.buckets.all()]
if bucket_name not in all_buckets:
    print(f"'{bucket_name}' bucket does not exist. creating now...")
    s3_resource.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": region})
    print(f"'{bucket_name}' bucket has been created.")

else:
    print(f"'{bucket_name}' bucket already exists. no need to create a new one.")
#bucket_list = s3_client.list_buckets()

#for bucket in bucket_list['Buckets']:
  #  print(bucket['Name'])
#pp.pprint(bucket_list)
