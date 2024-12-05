from hmac import new
import json
from sre_compile import isstring


def main_menu():
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Edit Inventory Item")
    print("4. Delete Item")
    print("5. Total Profit/Loss")
    print("6. Show Analytics")
    print("7. Exit\n")
    
    
def view_inventory():
    
    # Reading Data From The JSON File
    with open("C:\mydata\expenses.json", "r") as file:
        data = json.load(file)
        
    # Iterate through list of data
    for indice in data :
        print(f"Item Name:\t{indice['name']}")
        print(f"Cost:\t\t{indice['cost']}")
        print(f"Total Sold:\t{indice['sold']}")
        print(f"Profit/Loss:\t{indice['profit_loss']}")
        
    
def add_item() :
    with open("C:\mydata\expenses.json", "r") as file:
        data = json.load(file)

    item = input("Enter Name of Item:\t")
    cost = float(input("Enter Cost of Item:\t"))
    sold = float(input("Enter if Sold Item(s):\t"))
    profit_loss = sold - cost
    
    # Blank dict to add to list in json file
    new_dict = {"name" : item,
    "cost" : cost,
    "sold" : sold,
    "profit_loss" : profit_loss}
    
    data.append(new_dict)
    
    with open("C:\mydata\expenses.json", "w") as file:
        json.dump(data, file, indent=4)
        
    
def edit_item() :
    count = 0
    # Find Item to Edit
    find = input("Name of Item to Edit:\t")
    # Open JSON File
    with open("C:\mydata\expenses.json", "r") as file:
        data = json.load(file)
        
    # Search for data in list
    for name in data :
        if name['name'] == find :
            item = name
            break
        count = count + 1
      
    # Select which part of the dict to edit 
    choice = input("Type Edit (name), (cost), or (sold):\t")    
    edit = input("Enter new value:\t")
    
    #check if its supposed to be a number
    if edit[0].isdigit() :
        item[choice] = float(edit)
    else:
        item[choice] = edit
    # save data to the file
    data[count] = item
    
    with open("C:\mydata\expenses.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print("Success!\n{data[count]}")
    

def delete_item() :
    count = 0
    # Find Item to Edit
    find = input("Name of Item to Delete:\t")
    # Open JSON File
    with open("C:\mydata\expenses.json", "r") as file:
        data = json.load(file)
    # Search for data in list
    for name in data :
        if name['name'] == find :
            break
        count += 1
        
    data.pop(count)
    with open("C:\mydata\expenses.json", "w") as file:
        json.dump(data, file, indent=4)
        
    view_inventory()


def total_profit() :
    with open("C:\mydata\expenses.json", "r") as file:
        data = json.load(file)
    total = 0
    
    for cost in data :
        total += cost['profit_loss']
        
    print(f"Total Profit Is:\t{round(total, 2)}")
    

def analytics() :
    pass

def switch_case(user) :
    choice = {1 : add_item,
              2 : view_inventory,
              3 : edit_item,
              4 : delete_item,
              5 : total_profit,
              6 : analytics
              }
    return choice[user]()