import boto3
from botocore.exceptions import ClientError
import random
import sys
from os import environ, path
from dotenv import load_dotenv
bas_dir = path.abspath(path.dirname(__file__)) 
load_dotenv(path.join(bas_dir, '.env'))

class AWSFileUpload:
    bucket_name = environ.get("BUCKET_NAME", None)
    AWS_S3_ACCESS_KEY_ID = environ.get("AWS_S3_ACCESS_KEY_ID", None)
    AWS_S3_SECRET_ACCESS_KEY = environ.get("AWS_S3_SECRET_ACCESS_KEY", None)

    def get_url_of_file(self, fileName, attachment):
        try:
            s3 = boto3.resource('s3', region_name='ap-southeast-1', aws_access_key_id=self.AWS_S3_ACCESS_KEY_ID,
                                aws_secret_access_key=self.AWS_S3_SECRET_ACCESS_KEY)
            response = s3.Object(self.bucket_name, fileName).put(Body=attachment, ACL='public-read', Key=fileName)
            if response:
                location = boto3.client('s3', region_name="ap-south-1", aws_access_key_id=self.AWS_S3_ACCESS_KEY_ID,
                                        aws_secret_access_key=self.AWS_S3_SECRET_ACCESS_KEY).get_bucket_location(
                    Bucket=self.bucket_name)['LocationConstraint']
                key = fileName
                url = "https://s3-%s.amazonaws.com/%s/%s" % (location, self.bucket_name, key)
                print(url)
                return url
            else:
                return "Error in file upload"
        except Exception as e:
            
            print("line number of error is {}".format(sys.exc_info()[-1].tb_lineno), e)
            print(e)