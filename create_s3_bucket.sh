#!/bin/bash

# Stop execution on any error and echo commands
set -e
set -x

# Script to create an AWS S3 bucket
# Usage: ./create_s3_bucket.sh <bucket-name> [region]

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "Error: AWS CLI is not installed. Please install it first."
    exit 1
fi

# Check if user is authenticated with AWS
aws sts get-caller-identity &> /dev/null
if [ $? -ne 0 ]; then
    echo "Error: You're not authenticated with AWS. Please run 'aws configure' first."
    exit 1
fi

# Validate input parameters
if [ $# -lt 1 ]; then
    echo "Usage: $0 <bucket-name> [region]"
    echo "Example: $0 my-unique-bucket us-east-2"
    exit 1
fi

BUCKET_NAME=$1
REGION=${2:-us-east-2}  # Default to us-east-2 if region is not specified

# Validate bucket name according to S3 naming rules
if [[ ! $BUCKET_NAME =~ ^[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$ ]]; then
    echo "Error: Invalid bucket name. Bucket names must:"
    echo "- Contain only lowercase letters, numbers, dots (.), and hyphens (-)"
    echo "- Begin and end with a letter or number"
    echo "- Be between 3 and 63 characters long"
    exit 1
fi

echo "Creating S3 bucket '$BUCKET_NAME' in region '$REGION'..."

# Create the bucket
if [ "$REGION" = "us-east-1" ]; then
    # us-east-1 requires special handling (no LocationConstraint)
    aws s3api create-bucket --bucket "$BUCKET_NAME" --acl private
else
    aws s3api create-bucket --bucket "$BUCKET_NAME" --region "$REGION" \
    --create-bucket-configuration LocationConstraint="$REGION" --acl private
fi

# No need to check exit status with set -e, but we'll keep the success message
echo "S3 bucket '$BUCKET_NAME' created successfully!"
echo "Bucket URL: https://$BUCKET_NAME.s3.amazonaws.com"