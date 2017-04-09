#!/usr/bin/python

try:
  import boto3
  HAS_BOTO3 = True
except ImportError:
  HAS_BOTO3 = False

import pprint
import os

# Credentials & Region
#access_key = os.environ["access_key"]
#secret_key = os.environ["secret_key"]
access_key = ""
secret_key = ""
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
    supports_check_mode=False,
    mutually_exclusive=[],
    required_together=[]
  )
  
  access_key = module.params['access_key']
  secret_key = module.params['secret_key']

  msg = access_key + "----" + secret_key
  
  result = dict(changed=False, output=msg)
  module.exit_json(**result)
  
  


if __name__ == "__main__":
  test_main()
  
