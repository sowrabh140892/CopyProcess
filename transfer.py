import boto3
import json
import os
from os import environ
import re
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
S3_BUCKET_NAME = 'source1408'
VFX_VENDOR_TEST = 'destination1408'
aws_access_key_id=environ.get('aws_access_key_id')
aws_secret_access_key=environ.get('aws_secret_access_key')
session = boto3.Session(aws_access_key_id, aws_secret_access_key, region_name='us-east-1', )
print dir(session)
def receive_message_from_queue():
    """
    :return:
    """
    sqs_client = session.client('sqs')
    receive_response = sqs_client.receive_message(QueueUrl=COPY_BUCKET_QUEUE,
                                                  AttributeNames=['All'],
                                                  MaxNumberOfMessages=10,
                                                  VisibilityTimeout=5,
                                                  WaitTimeSeconds=10, )
    logger.info("Response: %s" % receive_response)
    return receive_response
def get_s3_bucket_object():
    """
    :return:
    """
    s3_client = session.client('s3')
    objects_list = s3_client.list_objects(Bucket=S3_BUCKET_NAME)
    if objects_list.get('Contents'):
        for obj_item in objects_list.get('Contents'):
            yield obj_item
def copy_to_vfx_vendor_test(bucket_key, source_bucket_name=S3_BUCKET_NAME, destination_bucket_name=VFX_VENDOR_TEST):
    """
    :param bucket_key:
    :param source_bucket_name:
    :param destination_bucket_name:
    :return:
    """
    s3_resource = session.resource('s3')
    copy_source = {
        'Bucket': source_bucket_name,
        'Key': bucket_key
    }
    bucket = s3_resource.Bucket(destination_bucket_name)
    obj = bucket.Object(bucket_key)
    print "Copying key %s" % bucket_key
    obj.copy(copy_source)
    print "Copy Completed!"
def main():
    """
    :return:
    """
    for each in get_s3_bucket_object():
        print each
        copy_to_vfx_vendor_test(bucket_key=each.get('Key'))
if __name__ == '__main__':
    main()
