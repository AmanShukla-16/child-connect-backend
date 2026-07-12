from pydantic import BaseModel
from typing import Optional


# -----------------------------
# Vendor Model
# -----------------------------
class Vendor(BaseModel):
    name: str
    category: str
    city: str
    phone: str

    description: Optional[str] = None
    fees: Optional[str] = None
    morning_batch: Optional[str] = None
    evening_batch: Optional[str] = None
    address: Optional[str] = None
    rating: Optional[float] = None
    image: Optional[str] = None


# -----------------------------
# Booking Model
# -----------------------------
class Booking(BaseModel):
    parent_name: str
    parent_phone: str
    vendor_id: int
    vendor_name: str
    booking_date: str
    batch_time: str


# -----------------------------
# Parent Registration Model
# -----------------------------
class Parent(BaseModel):
    name: str
    email: str
    phone: str
    password: str
#-----------------------------
# Parent login model
#-----------------------------

class LoginParent(BaseModel):
    email: str
    password: str