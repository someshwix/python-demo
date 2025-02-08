import boto3

def create_s3_bucket(bucket_name, region='eu-central-1'):
    # Create a new S3 client
    s3_client = boto3.client('s3', region_name=region)
    
    # Create the bucket
    try:
        response = s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )
        print(f'Bucket {bucket_name} created successfully in {region} region.')
    except Exception as e:
        print(f'Error creating bucket: {e}')

if __name__ == "__main__":
    bucket_name = 'copilot-demo-bucket'
    create_s3_bucket(bucket_name)