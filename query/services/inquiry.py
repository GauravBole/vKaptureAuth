
from query.models import Inquiry

class InquiryService:

    def create_inquiry(self, request_data):
        inquiry_model = Inquiry(**request_data)
        print(inquiry_model)
