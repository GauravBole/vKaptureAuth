import boto3
from botocore.exceptions import ClientError
import random
import sys

class AWSFileUpload:
    bucket_name = "gauarvblogimage"
    AWS_S3_ACCESS_KEY_ID = "AKIAJB22P6QJQJJQVAWA"
    AWS_S3_SECRET_ACCESS_KEY = "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"

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