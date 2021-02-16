from utils.s3_upload import AWSFileUpload

class PhotographerPortfolio:

    def upload_image(self, image):
        
        aws_upload = AWSFileUpload()
        file_name = image.name
        file_url = aws_upload.get_url_of_file(fileName=file_name, attachment=image)
        print(file_url)