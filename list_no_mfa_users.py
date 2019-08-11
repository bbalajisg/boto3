""" This script will print the list of IAM users who have console access but MFA not enabled.
Author: Kannan Anandakrishnan
Requirements: boto3 package installed, aws credentials configured.
"""

# Importing boto3 client
import boto3

# Creating boto3 handle for iam resource
IAM_CLIENT = boto3.client('iam')

def get_login(user):
    
    """ Checks whether user has login profile (console access). If exists, calls get_mfa func. 
    If no login profile exists, we will get NoSuchEntityException. Catch the error and pass.
        Parameters: user (string): Username of IAM user
    """

    try:
        response = IAM_CLIENT.get_login_profile(UserName=user)
        if response['LoginProfile']['UserName'] == user:
            get_mfa(user)
    except IAM_CLIENT.exceptions.NoSuchEntityException:
        pass

def get_mfa(user):

    """ Check the mfa devices attached to the user. If no mfa exists, print MFA not enabled.
        Parameters: user (string): Username of IAM user who has login profile enabled.
    """

    response = IAM_CLIENT.list_mfa_devices(UserName=user)
    if response['MFADevices'] != [] and "mfa" in response['MFADevices'][0]['SerialNumber']:
        pass
    else:
        print("MFA not enabled: {}".format(user))

if __name__ == '__main__':
# Use boto3 paginator option if number of users is very high. 
    DETAILS = IAM_CLIENT.list_users(MaxItems=250)
    for user_detail in DETAILS['Users']:
        get_login(user_detail['UserName'])
