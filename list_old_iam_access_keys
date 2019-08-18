""" This script will print the list of access keys older than 90 days.
Author: Kannan Anandakrishnan
Requirements: boto3 package installed, standard libraries - datetime, csv, and aws credentials configured.
"""

import datetime, boto3, csv

IAM = boto3.client('iam')

def access_key(user):

    """List the access key(s) of every user. Then iterate over the keys and pass the created date to time_diff()
    CreateDate of Access Key is a datetime object. Passing it as an input to time_diff func to get the age in days.
       Parameters: user (string) : Username of IAM user
    """
    keydetails=IAM.list_access_keys(UserName=user)

    # Some user may have 2 access keys. So iterating over them and listing the details of active access key.
    for keys in keydetails['AccessKeyMetadata']:
        if keys['Status']=='Active' and (time_diff(keys['CreateDate'])) >= 90:
            print (keys['UserName'],keys['AccessKeyId'], time_diff(keys['CreateDate']),sep=',')

def time_diff(keycreatedtime):
    # Getting the current time in utc format
    now=datetime.datetime.now(datetime.timezone.utc)

	# Calculating diff between two datetime objects.
    diff=now-keycreatedtime
    # Returning the difference in days
    return diff.days
	

if __name__ == '__main__':
    """ In this main function, we are fetching the users from IAM and passing the username to access_key() """
    
    # This returns a dictionary response
    details = IAM.list_users(MaxItems=300)

    # Header information
    print ("Username","AccessKey","Status","KeyAge",sep=',')
    for user in details['Users']:
        access_key(user['UserName'])
