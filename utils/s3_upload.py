import random
import sys
from os import environ, path

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

bas_dir = path.abspath(path.dirname(__file__)) 
load_dotenv(path.join(bas_dir, '.env'))

from typing import BinaryIO

from botocore.exceptions import NoCredentialsError


class AWSFileUpload:
    
    _AWS_KEY_ID = environ.get("AWS_KEY_ID", None)
    _AWS_ACCESS_KEY = environ.get("AWS_ACCESS_KEY", None)

    _BUCKET_NAME = "vkapture-v1"
    _AWS_REGION = "ap-south-1"

    _REGIN_ACCESS_ID_AND_KEY = {"region_name": _AWS_REGION, "aws_access_key_id": _AWS_KEY_ID,
                                "aws_secret_access_key": _AWS_ACCESS_KEY}


    def __init__(self, file:BinaryIO, file_name:str):
        self.file = file
        self.file_name = file_name


    def _make_filename_unique(self):

        if self.file_name != "" and self.file_name is not None:

            splitted = self.file_name.split('.')

            rand_int = random.randint(10000,99999)

            rand_int = str(rand_int)

            splitted[0]=splitted[0]+rand_int

            self.file_name = '.'.join(splitted)
            

    def upload_file(self):
        self._make_filename_unique()
        url_of_file = self._upload_s3_file_and_get_url()
        return url_of_file


    def _upload_s3_file_and_get_url(self):
        url = ""
        try:
            s3 = boto3.resource('s3', **self._REGIN_ACCESS_ID_AND_KEY)
            response = s3.Object(self._BUCKET_NAME, self.file_name).put(Body=self.file, ACL="public-read", Key=self.file_name)
            
            
            if response:
                location = boto3.client('s3', **self._REGIN_ACCESS_ID_AND_KEY).get_bucket_location(Bucket=self._BUCKET_NAME)['LocationConstraint']

                url = f"https://s3-{location}.amazonaws.com/{self._BUCKET_NAME}/{self.file_name}" 
        except Exception as e: 
            print("line number of error is {}".format(sys.exc_info()[-1].tb_lineno), e)
            print(e)
        return url
        


            