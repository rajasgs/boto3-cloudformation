

import boto3


if __name__ == '__main__':

    client = boto3.client('cloudformation', region_name="ap-northeast-1")
    
    response = client.describe_stacks(
        StackName='rjstack01',
        NextToken='string'
    )

    print(response)

