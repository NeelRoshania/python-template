import boto3

"""
Notes
    - client = boto3.client('s3')
    - s3 = boto3.resource('s3')

"""
    
def get_buckets(s3):
    return [bucket for bucket in s3.buckets.all()]

def get_objects(client, bucket: str):
    return client.list_objects_v2(
        Bucket=bucket,
        MaxKeys=100
)

def list_buckets(s3):
    return [bucket.name for bucket in s3.buckets.all()]