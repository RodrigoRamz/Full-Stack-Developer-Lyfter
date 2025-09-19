#menu.py
#print the menu and validates the chosen option

def show_menu(): #print all the program options
    print("\n=== Students Control System (OOP) ===")
    print("1) Add Students (one by one)")
    print("2) List Students")
    print("3) Top 3")
    print("4) Global Average")
    print("5) CSV Export")
    print("6) CSV Import (exported previously)")
    print("0) Exit")

def read_option(): #always ask for a valid option
    while True:
        s = input('Select an option: ').strip() #.strip() removes blank spaces
        if s.isdigit():
            return int(s)
        print('Invalid Option. Try again with options from 0 to 6.')
        