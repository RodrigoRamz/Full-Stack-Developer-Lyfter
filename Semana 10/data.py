#data.py (refactor without global variables)
#csv with DictWriter/DictReader; without global to schema neither route

import csv
import os

def export_csv(students, route, fieldnames): #Export the list of dicts to CSV using fieldnames and saving it in 'route'
    if not students:
        print('There is no data to export.')
        return
    try: #newline='' avoids extra white lines and utf-8 accent 
        with open(route, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=list(fieldnames))
            writer.writeheader() #writes the column rows
            rows = ({k: s.get(k, "") for k in fieldnames} for s in students)
            writer.writerows(rows) #each dit (register) to one row
        print(f"Data Exported in '{route}'")
    except OSError as s:
        print(f'Error when writing the CSV File: {s}') 

def import_csv(students, route, fieldnames): #import from CSV located in 'route' verifying that 'fieldnames' columns exists
    if not os.path.exists(route): #requisite if there is no file previously exported, then message
        print(f"There is no file previously exported. Route not found '{route}'")
        return
    try:
        with open(route, "r", newline="", encoding='utf-8') as f:
            reader = csv.DictReader(f) #each row -> dict whom keys are the headers
            if reader.fieldnames is None:
                print('CSV as no header.')
                return
            missing = [c for c in fieldnames if c not in reader.fieldnames]
            if missing:
                print(f'Missing columns in CSV: {missing}')
                return

            added = 0
            for row in reader:
                try: 
                    name = (row.get('name') or '').strip()
                    group = (row.get('group') or '').strip()
                    if not name or not group:
                        raise ValueError('name or group are empty')
                    #convert and validate grades 0-100
                    spa = int(row.get('spanish'))
                    eng = int(row.get('english'))
                    geo = int(row.get('geography'))
                    sci = int(row.get('sciences'))
                    for n in (spa, eng, geo, sci):
                        if not (0<= n <=100):
                            raise ValueError('grade is out of range (0-100)') 
                        #if everything is ok the register is added

                    students.append({
                        'name' : name, 
                        'group' : group,
                        'spanish' : spa, 
                        'english' : eng,
                        'geography': geo,
                        'sciences' : sci, 
                    })
                    added += 1
                except Exception as err: #reports the issue in a row then continue
                    print(f'Ignored Row: {row} -> {err}')
        print(f' Import Completed. Added Registers: {added}')
    except OSError as s:
        print(f'Error when reading the CSV file: {s}')