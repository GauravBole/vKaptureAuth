
from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, conint, constr, ValidationError, validator
from query.models import Inquiry
from models import User
class QuotationDetails(BaseModel):
    photographer = User
    quote : int
    message : str = None
    is_accepted : bool
    created_at : datetime

class Quotation(BaseModel):
    inquiry : int
    quotation : QuotationDetails
    is_active : bool = True


