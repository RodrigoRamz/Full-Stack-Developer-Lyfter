#menu.py
#print the menu and validates the chosen option

def show_menu(): #print all the program options
    print("\n=== Students Records ===")
    print("1) Add Students (one by one)")
    print("2) View All Students")
    print("3) Average Top 3")
    print("4) Global Average")
    print("5) CSV Export")
    print("6) CSV Import (exported previously)")
    print("0) Exit")

def read_valid_option(valid_options): #always ask for a valid option
    while True:
        option = input('Select an option: ').strip() #.strip() removes blank spaces
        if option in valid_options:
            return option
        print('Invalid Option. Try again with options from 0 to 6.')
        