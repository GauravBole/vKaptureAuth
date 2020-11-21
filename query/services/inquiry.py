from query.dao.inquiry import inquiryDao
from query.models import Inquiry, Address, InquiryDetail
from pydantic import parse_obj_as
from typing import List

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
        # print(list(all_inquires))
        # for i in all_inquires:
        #     detail_address = Address(**i)
        #     i['detail_address'] = detail_address
        #     print(InquiryDetail(**i))
        # inquiry_model = parse_obj_as(List[InquiryDetail], **(all_inquires))
        # inquiry_model = Inquires(**(all_inquires.dict()))
        print(all_inquires)
        return all_inquires
