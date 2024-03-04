import pandas as pd
import shutil
import os
from Classes.BuffPricesManager import BuffPricespullall, linepricespull
from Classes.currencyconverter import currencyConverter

csv_file_path = os.path.abspath('classes/investments.csv')
df = pd.read_csv(csv_file_path)
formatters = {}


def new_line_data():
    global df  # Declare df as a global variable
    # Input new data from the user
    goods_id = input("Enter goods ID: ")
    float_value = input("Enter float range (Min: 3 decimals): ")
    quantity = input("Enter quantity: ")
    buy_price_original = str(input("Enter buy price in EUR: "))
    buy_price_cny = currencyConverter(buy_price_original)
    # current_lowest_steam = input("Enter current lowest steam: ")
    # current_lowest_buff = input("Enter current lowest buff: ")
    # current_highest_buyorder = input("Enter current highest buyorder: ")
    # percentage_profit = input("Enter percentage profit: ")

    new_data = {
        "goods_name": "",
        "goods_id": [goods_id],
        "float_range": [float_value],
        "buy_price_original": [buy_price_original],
        "quantity": [quantity],
        "buy_price_cny": [buy_price_cny],
        "current_lowest_steam": "",
        "current_lowest_buff": "",
        "current_highest_buyorder": "",
        "percentage_profit": "",
        "inventory": True
    }
    return new_data


def add_new_line():
    global df

    new_data = new_line_data()
    new_row = pd.DataFrame(new_data)
    df = pd.concat([new_row, df], ignore_index=True)
    df.to_csv(csv_file_path, index=False)
    df.reset_index(drop=True, inplace=True)  # Reset the index after removing the row
    df.to_csv(csv_file_path, index=False)
    #run pullrequest data


def show_table():
    df = pd.read_csv(csv_file_path)
    print(df.to_string(formatters=formatters, justify="center"))


def edit(): #edit this menu still dont use if functions
    global df

    show_table()
    editingline = int(input("Enter the row to edit: "))
    print(df.iloc[[editingline]].to_string(formatters=formatters, justify="center"))
    print("Options:")
    print("1. Edit row")
    print("2. Update row")
    print("3. Sold row")
    print("4. Remove row")
    print("5. Cancel edit")
    edittask = input("Enter the number of your choice: ")

    if edittask == "1":
        new_data = new_line_data()
        # Convert new_data to a DataFrame
        new_row = pd.DataFrame(new_data)
        df = pd.concat([df.iloc[:editingline], new_row, df.iloc[editingline:]], ignore_index=True)
        df.to_csv(csv_file_path, index=False)
        # run pullrequest data
        print("Editing row...")

    if edittask == "2":
        df.iloc[[editingline]].to_string(formatters=formatters, justify="center")
        print(type(editingline))
        print(editingline)
        linepricespull(editingline)
        print(df.iloc[[editingline]].to_string(formatters=formatters, justify="center"))
        # run pullrequest data for just this row
        print("Updating row...")
    if edittask == "3":
        column_name = 'inventory'
        df.at[editingline, column_name] = not df.at[editingline, column_name]
        #print(df.iloc[[editingline]].to_string())
        df.to_csv(csv_file_path, index=False)
        print("Inventory status changed")
    if edittask == "4":
        df.drop(editingline, inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv(csv_file_path, index=False)
        print("Row removed")
    if edittask == "5":
        print("Quit editing")
        return


def update():
    print("Updating table...")
    BuffPricespullall()


def saveBackup():
    backup_path = 'classes/backupinvestments.csv'
    shutil.copyfile(csv_file_path, backup_path)
    print(f"Backup saved to {backup_path}")


def quit():
    print("Quitting the program...")
    exit()


def menustart(menu_ready):
    while True:
        print("Options:")
        print("1. Add Line")
        print("2. Show table")
        print("3. Edit")
        print("4. Update")
        print("5. Save to Backup")
        print("6. Quit")

        choice = input("Enter the number of your choice: ")
        switch = {
            '1': add_new_line,
            '2': show_table,
            '3': edit,
            '4': update,
            '5': saveBackup,
            '6': quit
        }
        selected_function = switch.get(choice)
        if selected_function:
            selected_function()
        else:
            print("Invalid choice. Please select a valid option.")