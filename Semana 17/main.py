import FreeSimpleGUI as sg
from Financial_Manager import FinancialManager

def refresh_main_view(window, manager: FinancialManager):
    """Update table and balance in the main window."""
    window["-TABLE-"].update(manager.to_table_values())
    balance = manager.calculate_balance()
    window["-BALANCE-"].update(f"{balance:.2f}")


def open_add_category_window(manager):
    layout = [
        [sg.Text("Add a New Category")],
        [sg.Text("Category Name:"), sg.Input(key="-NEW-CAT-")],
        [sg.Button("Save"), sg.Button("Cancel")]
        ]
    window = sg.Window("Add Category", layout, modal=True) #Blocks the main window to call to action

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            break

        elif event == "Save":
            category_name = values["-NEW-CAT-"]
            added = manager.add_category(category_name)

            if not added:
                sg.popup("Category not added:\n- It already exists or is empty.")
            else: 
                sg.popup("Category added successfully.")

            break
    
    window.close()

def open_add_transaction_window(manager: FinancialManager, transaction_type: str, main_window):
    """Open a modal window to add a new transaction.
    transaction_type: 'INCOME', 'EXPENDITURE'
    """
    layout = [
        [sg.Text(f"Add a new {transaction_type.title()}")],
        [sg.Text("Title:"), sg.Input(key="-TITLE-")],
        [sg.Text("Amount:"), sg.Input(key="-AMOUNT-")],
        [sg.Text("Date:"), sg.Input(key="-DATE-", size=(20, 1)),
            sg.CalendarButton("Select Date", target="-DATE-", format="%d/%m/%Y")],
        [sg.Text("Category:"), sg.Combo(manager.categories, key="-CATEGORY-", readonly=True)],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]

    window = sg.Window("Add Transaction", layout, modal=True)

    while True:
        event, values = window.read()
        
        if event in (sg.WIN_CLOSED, "Cancel"):
            break

        elif event == "Save":
            title = values["-TITLE-"]
            amount = values["-AMOUNT-"]
            date = values["-DATE-"]
            category = values["-CATEGORY-"]

            try:
                manager.add_transaction(
                    title=title, 
                    amount=amount,
                    transaction_type=transaction_type,
                    date=date, 
                    category=category,
                )
            except ValueError as e:
                sg.popup(str(e))
            else:
                sg.popup("Transaction saved successfully.")
                refresh_main_view(main_window, manager)
                break

    window.close()


manager = FinancialManager("finance.json")

layout = [
    [sg.Text("Welcome to your Personal Financial Manager", font=("Arial", 16))],
    [sg.Button("Add Income"), sg.Button("Add Expenditure"), sg.Button("Add Category")],
    [sg.Table(values=manager.to_table_values(), 
                headings=["Transaction Type", "Category", "Title", "Amount", "Date"], 
                key="-TABLE-",
                auto_size_columns=True
)],
    [sg.Text("Your current Balance is:"), sg.Text("0.00", key="-BALANCE-")], 
]

window = sg.Window("Finance Manager", layout, finalize=True)
refresh_main_view(window, manager)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == "Add Category":
        open_add_category_window(manager)

    elif event == "Add Income":
        open_add_transaction_window(manager, "INCOME", window)

    elif event == "Add Expenditure":
        open_add_transaction_window(manager, "EXPENDITURE", window)

window.close()