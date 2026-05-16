import boto3
import os

def upload_log_to_s3(file_data):
    """Uploads application logs to S3 bucket."""
    # CRITICAL SECURITY RISK: Hardcoded credentials
    AWS_ACCESS_KEY = "AKIAEXAMPLE123456789"
    AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    print(f"Connecting to S3 with key: {AWS_ACCESS_KEY}")
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    try:
        result = s3.put_object(Body=file_data, Bucket='your-bucket-name')['ResponseMetadata']['HTTPStatusCode']
        return result
    except Exception as e:
        raise e  # Re-raise the original exception instead of TypeError