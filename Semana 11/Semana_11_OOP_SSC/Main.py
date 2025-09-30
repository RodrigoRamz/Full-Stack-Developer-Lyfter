#main.py
#Input point: run the program calling the menu, actions and CSV data. 

from Actions import add_students, listing, top3, global_average
from Data import export_csv, import_csv
from Menu import show_menu, read_option

def main(): #database: dictionary list
    students = [] #valid options 0-6

    csv_path = 'students.csv'
    fieldnames = ('name', 'group', 'spanish', 'english', 'geography', 'sciences') #this variables are now locals and not globals in data.py 
    
    while True:
        show_menu()
        opt = read_option()

        if opt == 0:
            print('Bye!')
            break
        elif opt == 1:
            add_students(students)
        elif opt == 2:
            listing(students)
        elif opt == 3:
            top3(students)
        elif opt == 4:
            global_average(students)
        elif opt == 5:
            export_csv(students, route=csv_path, fieldnames=fieldnames)
        elif opt == 6:
            import_csv(students, route=csv_path, fieldnames=fieldnames)
        else:
            print('Unknown option. Try again.')


if __name__ == '__main__':
    main()