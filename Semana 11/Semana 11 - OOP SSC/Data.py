#data.py (refactor without global variables)
#csv with DictWriter/DictReader; without global to schema neither route

import csv
import os
from Models.Student import Student

def export_csv(students, *, route, fieldnames): #Export the list of dicts to CSV using fieldnames and saving it in 'route'
    try: #newline='' avoids extra white lines and utf-8 accent 
        with open(route, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for s in students:
                writer.writerow(s.to_dict()) #each dit (register) to one row
        print(f"Data Exported {len(students)} students to '{route}'.")
    except OSError as e:
        print(f'Error when exporting the CSV File: {e}') 

def import_csv(students, *, route, fieldnames): #import from CSV located in 'route' verifying that 'fieldnames' columns exists
    if not os.path.exists(route): #requisite if there is no file previously exported, then message
        print(f"There is no file previously imported. Route not found '{route}'")
        return
    try:
        with open(route, "r", newline="", encoding='utf-8') as f:
            reader = csv.DictReader(f) #each row -> dict whom keys are the headers
            if not reader.fieldnames:
                print('CSV as no header.')
                return
            
            missing = [col for col in fieldnames if col not in reader.fieldnames]
            if missing:
                print(f'Missing columns in CSV: {missing}')
                return

            added = failed = 0
            for row in reader:
                try:
                    st = Student.from_dict(row)
                    students.append(st)
                    added += 1
                except ValueError:
                    failed += 1
            print(f'Imported: {added} students. Failed: {failed}.')
    except OSError as e:
        print(f'Error importing CSV: {e}')