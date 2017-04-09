#!/usr/bin/python

try:
  import boto3
  HAS_BOTO3 = True
except ImportError:
  HAS_BOTO3 = False

import pprint
import os

# Credentials & Region
access_key = os.environ["AWS_ACCESS_KEY_ID"]
secret_key = os.environ["AWS_SECRET_ACCESS_KEY"]
region = os.environ["AWS_DEFAULT_REGION"]

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

from ansible.module_utils.basic import *
from ansible.module_utils.ec2 import boto3_conn, ec2_argument_spec, get_aws_connection_info, camel_dict_to_snake_dict

def test_main():
  argument_spec = ec2_argument_spec()
  argument_spec.update(
    dict(      
      params=dict(type='dict', required=False, default={}, aliases=['method_params']),
      convert_param_case=dict(required=False, default=None, choices=['camel', 'Pascale'])
    )
  )
						   
  module = AnsibleModule(
    argument_spec=argument_spec,
    supports_check_mode=True,
    mutually_exclusive=[],
    required_together=[]
  )
  
  msg = "play done"  
  
  result = dict(changed=False, output=msg)
  module.exit_json(**result)
  
  


if __name__ == "__main__":
  test_main()
  
