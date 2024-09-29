#!/usr/bin/env python3

import requests
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

#Get the URL from the user input
file_url = input("URL of file: ")

file_name = file_url.split("/")[-1]

response = requests.get(file_url,stream=True)
with open(file_name, 'wb') as file:
  for chunk in response.iter_content(chunk_size=8192):
    file.write(chunk)

print(f"{file_name}")

bucket_name = "ds2022-pnr3kr"
object_name = f"uploads/{file_name}"


s3 = boto3.client('s3')

with open(file_name, 'rb') as file_data:
  s3.put_object(
    Body=file_data,
    Bucket=bucket_name,
    Key=object_name,
    ACL='public-read'
)

expires_in = 604800

response = s3.generate_presigned_url(
  'get_object',
  Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)

print(f"{response}")
