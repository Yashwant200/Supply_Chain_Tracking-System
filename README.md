# Supply Chain Tracking System

## Project Overview

The **Supply Chain Tracking System** is a Python-based console application designed to track shipments across multiple stages of a supply chain. It provides end-to-end visibility, maintains shipment history, generates reports, and ensures efficient management of shipments.

This system is ideal for logistics companies, warehouses, or any organization needing to track goods from origin to delivery.

---

## Features

* **Add Shipment:** Create a new shipment with a unique ID, origin, and destination.
* **Track Shipment:** Retrieve shipment details by ID.
* **Update Shipment:** Update shipment status with timestamps.
* **View Shipment History:** Display chronological history of all updates.
* **Generate Reports:** Summarize shipment status counts and export reports.
* **Error Handling:** Custom exceptions for invalid operations, duplicate shipments, or incorrect statuses.
* **Unique ID Generation:** Each shipment receives a unique identifier using UUID.
* **File Export:** Save shipment reports to a date-stamped text file.

---

## Technologies & Concepts

* **Python 3.10+**
* Object-Oriented Programming (OOP)
* Exception Handling (`try/except`)
* Data Structures: `dict` and `list`
* File Handling
* Modular project structure
* UUID for unique shipment IDs
* Date and time management

---

## Project Structure

```
supply_chain_tracking_system/
│
├── main.py                          # Entry point, menu-driven interface
├── core/                             # Core modules
│   ├── tracker.py                   # Tracker class: manages multiple shipments
│   ├── utils.py                     # Helper utilities (ID generation, validation)
│   └── report.py                    # Report generation & export functions
├── models/
│   └── shipment.py                  # Shipment class and history tracking
├── exceptions/
│   └── exceptions.py                # Custom exception classes
├── reports_file_archive/            # Folder to save generated shipment reports
└── README.md                        # Project overview & instructions
```
---

## Usage

### Menu Options

1. **Add Shipment**

   * Enter origin and destination.
   * Shipment is assigned a unique ID automatically.

2. **Track Shipment**

   * Enter the shipment ID to view details and current status.

3. **Update Shipment**

   * Enter shipment ID and a valid status (`Created`, `In-Transit`, `Delivered`, `Delayed`).
   * Status is saved with a timestamp.

4. **View Shipment History**

   * Enter shipment ID to display all updates chronologically.

5. **Generate Report**

   * Generates a summary of all shipments.
   * Optionally exports the report as `reports/report_DD_MM_YYYY.txt`.

6. **Exit**

   * Quit the program safely.

---

## Example

```
---------------Menu---------------
1. Add Shipment
2. Track Shipment
3. Update Shipment
4. View Shipment History
5. Generate Report
6. Exit

Enter the functionality number to access it: 1
Enter the Origin Of The Shipment: Delhi
Enter The Destination Of The Shipment: Mumbai
New Shipment Is Created With Unique ID SHP-A1B2C3

Enter the functionality number to access it: 3
Enter The Shipment ID: SHP-A1B2C3
Enter Valid Status To Be Change: In-Transit
Shipment Status Updated Successfully

Enter the functionality number to access it: 4
Enter The Shipment ID: SHP-A1B2C3
History for SHP-A1B2C3:
1. Created - 04/10/2025 10:15:00
2. In-Transit - 04/10/2025 12:30:00

Enter the functionality number to access it: 5
Shipment Summary Report:
Created: 0
In-Transit: 1
Delivered: 0
Delayed: 0
Report saved as: reports/report_04_10_2025.txt
```