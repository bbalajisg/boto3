# This script will print the location, logging, versioning details of all the buckets in your AWS account


import boto3
import sys

S3 = boto3.client('s3')

# Gets bucket name as argument, prints the bucket location, logging and versioning status by calling respective methods of S3.
def get_bucket_info(bucket_name):
	print (f"Bucket Name: {bucket_name}")
	print ("Location: ", S3.get_bucket_location(Bucket=bucket_name)['LocationConstraint'])
	print ("Logging: ", S3.get_bucket_logging(Bucket=bucket_name).get('LoggingEnabled','Not enabled'))
	print ("Versioning: ", S3.get_bucket_versioning(Bucket=bucket_name).get('Status', 'Not enabled'))
	print ("\n")

# Using S3 boto3 client, listing all the buckets information.
# Iterating over the buckets list to get bucket metadata and pass the bucket name as argument to get_bucket_info function

if __name__ == '__main__':
	for BUCKETS in S3.list_buckets()['Buckets']:
		get_bucket_info(BUCKETS['Name'])