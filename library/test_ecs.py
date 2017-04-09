#!/usr/bin/python

try:
  import boto3
  HAS_BOTO3 = True
except ImportError:
  HAS_BOTO3 = False

import pprint
import os

# Credentials & Region
access_key = os.environ["access_key"]
secret_key = os.environ["secret_key"]
region = "us-east-1"

# ECS Details
cluster_name = "BotoCluster"
service_name = "service_hello_world"
task_name = "hello_world"

# Let's use Amazon ECS
'''
ecs_client = boto3.client(
    'ecs',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region
)
'''

def test_main():
  pprint.pprint("region : ") 
  pprint.pprint(region) 


if __name__ == "__main__":
    test_main()
    
