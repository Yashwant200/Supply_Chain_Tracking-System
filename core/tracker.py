"""
tracker.py
Contains the Tracker class to manage multiple shipments.

Responsibilities:
- Add a shipment
- Retrieve shipment by ID
- Update shipment status
- Generate a report summary of all shipments
"""

from exceptions import exceptions

class Tracker:
    def __init__(self):
        
        """Initialize an empty dictionary for storing shipments,
        in a dictionary with shipment_id as key.
        """
        self.shipments = {}

    def add_shipment(self, shipment):
        
        """
       Add a Shipment object to the tracker.
       Raises: DuplicateShipmentError: If shipment_id already exists.
       """
       
        if shipment.shipment_id in self.shipments:
            raise exceptions.DuplicateShipmentError(shipment.shipment_id)
        self.shipments[shipment.shipment_id] = shipment

    def get_shipment_by_id(self, shipment_id):
        
        """
        Retrieve a shipment by its ID.

        Args: Shipment_id (str): The shipment ID to lookup.

        Returns: Shipment: The shipment object.

        Raises: ShipmentNotFoundError: If shipment ID does not exist.
        """
        
        if shipment_id not in self.shipments:
            raise exceptions.ShipmentNotFoundError(shipment_id)
        return self.shipments[shipment_id]

    def update_shipment_status(self, shipment_id, status):
        
        """
        Update the status of a shipment.

        Args:
            shipment_id (str): Shipment ID.
            status (str): New valid status.
        """
        
        updated_shipment = self.get_shipment_by_id(shipment_id)
        updated_shipment.update_status(status)


    def generate_report(self):
       
        """
       Generate a formatted summary of all shipments.
       Returns:str: Formatted report with shipment details.
       """
       
        report_lines = []
        for ID, obj in self.shipments.items():
            report_lines.append(
                f"Shipment ID: {ID}\nOrigin: {obj.origin}\nDestination: {obj.destination}\nStatus: {obj.status}\n"
            )
        return "\n".join(report_lines) if report_lines else "No shipments available."