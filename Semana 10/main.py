#main.py
#Input point: run the program calling the menu, actions and CSV data. 

from menu import show_menu, read_valid_option
from actions import (
    add_students, 
    listing, 
    top3, 
    global_average, 
)
from data import export_csv, import_csv

def main(): #database: dictionary list
    students = [] #valid options 0-6
    csv_path = 'students.csv' 
    fieldnames = ('name', 'group', 'spanish', 'english', 'geography', 'sciences') #this variables are now locals and not globals in data.py 
    
    valid_options = {'0', '1', '2', '3', '4', '5', '6'} #menu loop: repeated until the user chose No to exit (break)
    while True:
        show_menu()
        option = read_valid_option(valid_options)

        if option == '0':
            print('Bye')
            break
        elif option == '1':
            add_students(students)
        elif option == '2':
            listing(students)
        elif option == '3':
            top3(students)
        elif option == '4':
            global_average(students)
        elif option == '5':
            export_csv(students)
        elif option == '6':
            import_csv(students)


if __name__ == '__main__':
    main()
