#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: raja
Source:

    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.validate_template

    aws cloudformation validate-template --template-body file://template/ec2_one.json
'''

# Import necessary modules
import boto3
import json

def get_template_json():

    with open('template/ec2_one.json') as f:
        data = json.load(f)

    return data

def startpy():
    
    client = boto3.client('cloudformation', region_name="ap-northeast-1")

    template_object = get_template_json()

    response = client.validate_template(
        TemplateBody = template_object,
        TemplateURL = 'string'
    )

    print(response)


if __name__ == '__main__':
    startpy()