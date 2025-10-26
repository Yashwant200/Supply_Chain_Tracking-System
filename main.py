"""
main.py
Entry point for the Supply Chain Tracking System.

This module provides a menu-driven interface for:
1. Adding a new shipment
2. Tracking shipments
3. Updating shipment status
4. Viewing shipment history
5. Generating shipment summary reports
"""

from core.tracker import Tracker
from core import utils, report
from models import shipment
from exceptions import exceptions

# Initialize Tracker object to manage shipments
tracker_obj = Tracker()

def main():
    
    """
   Main loop to display menu and handle user actions.
   Continues until the user selects Exit.
   """
   
    while True:
        # Display menu
        print("\n---------------Menu---------------")
        print("1. Add Shipment")
        print("2. Track Shipment")
        print("3. Update Shipment")
        print("4. View Shipment History")
        print("5. Generate Report")
        print("6. Export Report")
        print("7. Exit")

        try:
            choice = int(input("\nEnter the functionality number: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1–6.")
            continue
        
        # Add a new shipment
        if choice == 1:
            origin = input("\nEnter the Origin Of The Shipment: ")
            destination = input("Enter The Destination Of The Shipment: ")
            new_id = utils.generate_shipment_id()  # Generate unique ID
            new_shipment = shipment.Shipment(new_id, origin, destination)
            try:
                tracker_obj.add_shipment(new_shipment)
                print(f"\nNew Shipment Created With ID {new_id}")
            except exceptions.DuplicateShipmentError as e:
                print(e)
        
        # Track a shipment by ID
        elif choice == 2:
            ship_id = input("\nEnter The Shipment ID: ")
            try:
                found = tracker_obj.get_shipment_by_id(ship_id.strip())
                print("\nShipment Found!\n")
                print(f"Origin: {found.origin}\nDestination: {found.destination}\nStatus: {found.status.title()}")
            except exceptions.ShipmentNotFoundError as e:
                print(e)
        
        # Update shipment status
        elif choice == 3:
            check_ship_id = input("\nEnter The Shipment ID: ")
            change_status = input("Enter Valid Status To Be Changed: ")
            try:
                utils.validate_status(change_status)
                tracker_obj.update_shipment_status(check_ship_id, change_status)
                print("\nShipment Status Updated Successfully")
            except exceptions.ShipmentNotFoundError as e:
                print(e)
            except exceptions.InvalidStatusError as e:
                print(e)
        
        # View shipment history
        elif choice == 4:
            view_ship_id = input("\nEnter The Shipment ID: ")
            try:
                view_shipment = tracker_obj.get_shipment_by_id(view_ship_id.strip())
                print("\nShipment History:\n")
                for updates in view_shipment.get_history():
                    print(updates)
            except exceptions.ShipmentNotFoundError as e:
                print(e)
        
        # Generate shipment summary report
        elif choice == 5:
            summary = report.generate_shipment_report(tracker_obj.shipments)
            print("\nShipment Report:\n")
            print(summary)
        
        # Export the report to text file
        elif choice == 6:
            export_report = report.generate_shipment_report(tracker_obj.shipments)
            saved_path = report.export_to_file(export_report)
            print(f"\nThe report file has been created with name: {saved_path}")

        
        # Exit the program
        elif choice == 7:
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()