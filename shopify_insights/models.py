from pydantic import BaseModel
from typing import List, Optional, Dict

class ContactDetails(BaseModel):
    emails: List[str]
    phones: List[str]

class BrandContext(BaseModel):
    website: str
    brand_name: str
    product_catalog: List[dict] = []
    hero_products: List[str] = []
    privacy_policy: Optional[str] = None
    return_policy: Optional[str] = None
    faq: Optional[str] = None
    social_links: List[str] = []
    contact_details: ContactDetails
    about: Optional[str] = None
    contact: Optional[str] = None
    blog: Optional[str] = None
    order_tracking: Optional[str] = None