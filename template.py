#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: raja
Source:

    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.validate_template
'''

# Import necessary modules


def startpy():
    

    response = client.validate_template(
        TemplateBody='string',
        TemplateURL='string'
    )


if __name__ == '__main__':
    startpy()