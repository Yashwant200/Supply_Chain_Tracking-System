"""
utils.py
--------
Utility functions for shipment operations.
- Generate unique shipment IDs
- Validate shipment statuses
"""

import uuid
from exceptions import exceptions

def validate_status(status):
    
    """
   Validate a shipment status.
   
   status : The status to validate.
   
   InvalidStatusError : If status is not one of the allowed ones.
       
   Returns True if status is valid.
   """
   
    allowed_status = ["created", "in-transit", "delivered", "delayed","intransit"]
    if status.lower().strip() not in allowed_status:
        raise exceptions.InvalidStatusError(status)
    return True

def generate_shipment_id(prefix="SHP"):
    
    """
   Generate a unique shipment ID.

   prefix : Prefix for the shipment ID ("SHP").

   Returns a Unique shipment ID.
   """
   
    unique_id = uuid.uuid4().hex[:6].upper()
    return f"{prefix}-{unique_id}"
