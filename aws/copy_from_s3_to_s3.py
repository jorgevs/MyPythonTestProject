import boto3

# Source AWS account credentials and S3 bucket details
source_profile = 'Dev_Profile'  # Replace with your source AWS CLI profile
source_bucket_name = 'forr-dev-sagemaker-models-registry'
source_object_key = 'forrsight/models/lm_embedding_vector_model-2024-01-14.pkl'

# Destination AWS account credentials and S3 bucket details
dest_profile = 'Prod_Profile'  # Replace with your destination AWS CLI profile
dest_bucket_name = 'forr-prod-sagemaker-models-registry'
dest_object_key = 'forrsight/models/lm_embedding_vector_model-2024-01-14.pkl'

# Create Boto3 session with source AWS credentials
source_session = boto3.Session(profile_name=source_profile)
source_s3 = source_session.resource('s3')

# Create Boto3 session with destination AWS credentials
dest_session = boto3.Session(profile_name=dest_profile)
dest_s3 = dest_session.resource('s3')

# Download object from source bucket
source_bucket = source_s3.Bucket(source_bucket_name)
source_object = source_bucket.Object(source_object_key)
download_path = 'c:/tempJVS/lm_embedding_vector_model-2024-01-14.pkl'  # Specify the local path where the object will be downloaded
source_object.download_file(download_path)

# Upload object to destination bucket
dest_bucket = dest_s3.Bucket(dest_bucket_name)
dest_object = dest_bucket.Object(dest_object_key)
dest_object.upload_file(download_path)

print("Object uploaded successfully.")
