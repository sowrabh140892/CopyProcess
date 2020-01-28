import boto3
import json
import os
from os import environ
import re
import logging
import sys


logger = logging.getLogger()
logger.setLevel(logging.INFO)
source_bucket_key=str(sys.argv[1])
destination_bucket_key=str(sys.argv[2])
source_bucket_name=str(sys.argv[3])
destination_bucket_name=str(sys.argv[4])
aws_access_key_id=environ.get('aws_access_key_id')
aws_secret_access_key=environ.get('aws_secret_access_key')
session = boto3.Session(aws_access_key_id, aws_secret_access_key, region_name='us-east-1', )
print dir(session)

def copy_to_vfx_vendor_test(source_bucket_key, destination_bucket_key, source_bucket_name, destination_bucket_name):
    """
    :param bucket_key:
    :param source_bucket_name:
    :param destination_bucket_name:
    :return:
    """
    s3_resource = session.resource('s3')
    copy_source = {
        'Bucket': source_bucket_name,
        'Key': source_bucket_key
    }
    bucket = s3_resource.Bucket(destination_bucket_name)
    obj = bucket.Object(destination_bucket_key)
    print "Copying key %s" % source_bucket_key
    obj.copy(copy_source)
    print "Copy Completed!"

def main():
    """
    :return:
    """
    copy_to_vfx_vendor_test(source_bucket_key, destination_bucket_key, source_bucket_name, destination_bucket_name)
if __name__ == '__main__':
    main()
