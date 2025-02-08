import boto3

# Create an S3 resource and client
#s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

# List all S3 buckets
#for bucket in s3.buckets.all():
#    print(bucket.name)

# Define the CORS configuration
cors_config = {
    'CORSRules': [
        {
            'AllowedHeaders': ['Authorization'],
            'AllowedMethods': ['GET', 'PUT'],
            'AllowedOrigins': ['*'],
            'ExposeHeaders': ['GET', 'PUT'],
            'MaxAgeSeconds': 3000
        }
    ]
}

# Apply CORS configuration to the correct bucket
bucket_name = 'mynamebucket'  # Make sure this bucket exists
s3_client.put_bucket_cors(Bucket=bucket_name, CORSConfiguration=cors_config)

# Retrieve and print CORS configuration for the bucket
result = s3_client.get_bucket_cors(Bucket=bucket_name)
print(result)