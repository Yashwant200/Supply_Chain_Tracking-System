"""
shipment.py
-----------
Represents a single shipment in the system.
Each shipment has an 
- ID
- origin
- destination
- status
- history
"""

from datetime import datetime
from core.utils import validate_status

class Shipment:
    def __init__(self, shipment_id, origin, destination):
        
        """
        Initialize shipment with ID, origin, and destination.
        Logs an initial status "Created" in history.

        shipment_id : Unique identifier for the shipment.
        origin : Starting location.
        destination : Ending location.
        """
        
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.history = []  # List of status updates
        self.update_status("Created")
    
    @property
    def status(self):
        """
        Return the latest status of the shipment.
        """
        return self.history[-1]["status"] if self.history else None

    def update_status(self, status):
        
        """
       Update shipment status and append it to history.

       status : New status of the shipment.
       """
       
        validate_status(status)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append({"status": status, "time": timestamp})
        

    def get_history(self):
        
        """
        Return the full history of the shipment.
        
        list of dict Each dict has 'status' and 'time' keys.
        """
        
        return self.history
