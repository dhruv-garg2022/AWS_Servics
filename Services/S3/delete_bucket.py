
import boto3

def delete(name, access_id,secret_id):
    s3_client = boto3.client("s3",aws_access_key_id=access_id, aws_secret_access_key = secret_id)
# def delete(name):
#     s3_client = boto3.client("s3")
    objects = s3_client.list_objects_v2(Bucket=name)
    count = objects['KeyCount']

    if count == 0:
        response = s3_client.delete_bucket(Bucket=name)
        print("Deleting bucket")
    else:
        print("Empty your bucket")

# delete('dhruv123456garg')