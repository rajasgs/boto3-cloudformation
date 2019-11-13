

'''
    https://stackoverflow.com/questions/23019166/boto-what-is-the-best-way-to-check-if-a-cloudformation-stack-is-exists
'''

import boto3
from botocore.exceptions import ClientError

client = boto3.client('cloudformation', region_name="ap-northeast-1")

def stack_exists(name, required_status = 'CREATE_COMPLETE'):
    try:
        data = client.describe_stacks(StackName = name)
    except ClientError:
        return False

    return data['Stacks'][0]['StackStatus'] == required_status

if __name__ == '__main__':
    
    content = stack_exists('rjstack01')
    print(content)