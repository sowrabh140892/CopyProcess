import boto3
import json
import os
from os import environ
import re
import logging
import sys 


logger = logging.getLogger()
logger.setLevel(logging.INFO)
S3_BUCKET_NAME = environ.get('source_bucket')
VFX_VENDOR_TEST = environ.get('destination_bucket')
KEY = str(sys.argv[1])
aws_access_key_id=environ.get('aws_access_key_id')
aws_secret_access_key=environ.get('aws_secret_access_key')
session = boto3.Session(aws_access_key_id, aws_secret_access_key, region_name='us-east-1', )
print dir(session)

def copy_to_vfx_vendor_test(bucket_key=KEY, source_bucket_name=S3_BUCKET_NAME, destination_bucket_name=VFX_VENDOR_TEST):
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
    copy_to_vfx_vendor_test()
if __name__ == '__main__':
    main()
