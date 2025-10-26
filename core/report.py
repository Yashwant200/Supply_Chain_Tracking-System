"""
report.py
---------
Generate shipment summary reports.
"""

from datetime import datetime
import os

def generate_shipment_report(shipments):
    
    """
    Generate a summary report of shipment statuses.

    shipments : Dictionary of all Shipment objects and their 
    corrosponding keys (shipment id).
   
    Returns a formated string
    """
    
    report_lines = []
    for ID, obj in shipments.items():
        report_lines.append(
            f"Shipment ID: {ID}\nOrigin: {obj.origin}\nDestination: {obj.destination}\nStatus: {obj.status}\n"
        )
    return "\n".join(report_lines) if report_lines else "No shipments available."

def export_to_file(report_data, filename="report", folder='reports_file_archive'):
   
    """
    Export shipment report to a plain text file.

    report_data : Formated string 
    filename : Name of the file to save the report into (default is "report.txt").
    
    """

    today = datetime.now().strftime("%d_%m_%Y")
    full_filename = f"{filename}_{today}.txt"
    full_path = os.path.join(folder, full_filename)
    
    with open(full_path, 'w') as f:
        f.write("Shipment Report\n")
        f.write("====================\n")
        f.write(report_data)
    
    return filename