from query.dao.inquiry import inquiryDao
from query.models import Inquiry, Address, InquiryDetail

class InquiryService:

    def create_inquiry(self, request_data):
        address_model = Address(**request_data)
        request_data['detail_address'] = address_model
        request_data['status'] = 'Created'
        inquiry_model = Inquiry(**request_data)
        print(inquiry_model)
        inquiry_dao = inquiryDao()  
        inquiry_dao.create_inquiey(request_date=request_data)

    
    def get_all_inquires(self):
        inquiry_dao = inquiryDao()
        all_inquires = inquiry_dao.get_all_inquiry()
        inquiry_model = InquiryDetail(**(all_inquires.dict()))
        print(inquiry_model)
        return all_inquires
