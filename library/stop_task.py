#!/usr/bin/python

try:
  import boto3
  HAS_BOTO3 = True
except ImportError:
  HAS_BOTO3 = False

import pprint
import os

# Credentials & Region
access_key = ""
secret_key = ""
region = ""

# ECS Details
cluster_name = ""

# Let's use Amazon ECS
ecs_client = boto3.client(
  'ecs',
  aws_access_key_id=access_key,
  aws_secret_access_key=secret_key,
  region_name=region
)

from ansible.module_utils.basic import *
from ansible.module_utils.ec2 import boto3_conn, ec2_argument_spec, get_aws_connection_info, camel_dict_to_snake_dict

def test_main():
  argument_spec = ec2_argument_spec()
  argument_spec.update(
    dict(
      access_key = dict(type='str', required=True),
      secret_key = dict(type='str', required=True),
      cluster_name = dict(type='str', required=True),
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
  
  response = client.list_tasks(
    cluster=cluster_name,
    desiredStatus='RUNNING'
  )
  
  task_arn = response['taskArns'][0]
  
  response = client.stop_task(
    cluster=cluster_name,
    task=task_arn,
    reason='Stop by BMX'
)

  msg = "Task Stop"
	  
  result = dict(changed=False, output=msg)
  module.exit_json(**result)

if __name__ == "__main__":
  test_main()

