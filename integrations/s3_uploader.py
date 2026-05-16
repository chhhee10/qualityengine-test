import os

def upload_log_to_s3(file_data):
    """Uploads application logs to S3 bucket."""
    # CRITICAL SECURITY RISK: Hardcoded credentials
    AWS_ACCESS_KEY = "AKIAEXAMPLE123456789"
    AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    print(f"Connecting to S3 with key: {AWS_ACCESS_KEY}")
    # ... upload logic ...
    return True
