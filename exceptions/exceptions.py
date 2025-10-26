"""
exceptions.py
-------------
Custom exceptions for the Supply Chain Tracking System.
"""

class ShipmentNotFoundError(Exception):
    
    """Raised when a shipment is not found in the tracker."""
    
    def __init__(self, shipment_id_not_found):
        super().__init__(f"The Shipment With ID {shipment_id_not_found} Does Not Exist.")

class InvalidStatusError(Exception):
    
    """Raised when an invalid status is provided."""
    
    def __init__(self, status_exception):
        super().__init__(
            f'The Entered Status "{status_exception}" Is Not Valid.\nValid Statuses: ["Created", "In-Transit", "Delivered", "Delayed"]'
        )

class DuplicateShipmentError(Exception):
    
    """Raised when a duplicate shipment ID is added."""
    
    def __init__(self, shipment_id_duplicate):
        super().__init__(f"The Shipment With ID {shipment_id_duplicate} Already Exists.")
