
from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel
from query.models import Inquiry
from models import User
import datetime
class QuotationDetails(BaseModel):
    photographer_id : int
    quote : int
    message : str = ""
    is_accepted : bool = False
    created_at = datetime.datetime.now()
class Quotation(BaseModel):
    inquiry_id : int
    quotation : QuotationDetails
    is_active : bool = True


