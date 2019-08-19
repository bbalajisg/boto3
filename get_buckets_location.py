import boto3

S3 = boto3.client('s3')

details = S3.list_buckets()

def get_loc(bucketname):
	print(bucketname,S3.get_bucket_location(Bucket=bucketname)['LocationConstraint'])

for BUCKET_INFO in details['Buckets']:
	get_loc((BUCKET_INFO['Name']))
