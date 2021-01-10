from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, conint, constr, ValidationError, validator
# from models import User

class State(BaseModel):
    name: str
    code: str

class District(BaseModel):
    name: str
    code: str
    
class Address(BaseModel):
    address: str
    city: str = None
    zip_code: str
    state_id: int
    district_id: int

class EventCategory(BaseModel):
    name: str
    code: str

class InquiryStatus(str, Enum):
    Created = 'Created'
    Edited = 'Edited'
    SendQuery = 'Send Query'
    ReceivedQuotation = 'Received Quotation'
    AcceptQuotation = 'Accept Quotation'
    Expired = 'Expired'

class Inquiry(BaseModel):
    # query_id: str
    event_category_id: int
    title: str
    extra_message: str
    budget: str
    from_time: datetime
    to_time: datetime
    status: InquiryStatus
    detail_address: Address
    created_by_id: int

class InquiryEdit(BaseModel):
    # query_id: str
    event_category_id: int
    title: str
    extra_message: str
    budget: str
    from_time: datetime
    to_time: datetime
    # status: InquiryStatus().Updated
    # detail_address: Address
    created_by_id: int


class InquiryDetail(BaseModel):
    query_id: str 
    # event_category: EventCategory
    title: str
    extra_message: str
    budget: str
    from_time: datetime
    to_time: datetime
    # status: InquiryStatus
    detail_address: Address
    # created_by_id: User


# class Inquires(BaseModel):
#     inquires = List[InquiryDetail]