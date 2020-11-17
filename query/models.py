from datetime import datetime
from enum import Enum
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
    state_id: State
    district_id: District

class EventCategory(BaseModel):
    name: str
    code: str

class InquiryStatus(str, Enum):
    Created = 'Created'
    SendQuery = 'Send Query'
    ReceivedQuotation = 'Received Quotation'
    AcceptQuotation = 'Accept Quotation'
    Expired = 'Expired'

class Inquiry(BaseModel):
    query_id: str
    # event_category_id: EventCategory
    title: str
    extra_message: str
    budget: str
    from_time: datetime
    to_time: datetime
    # status: InquiryStatus
    # adddress_id: Address
    # created_by_id: User