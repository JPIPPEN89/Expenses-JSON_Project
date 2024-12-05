from tkinter import N
import main_functions
import json



user_input = 100
while user_input != 0 :
    user_input = int(input("Select 0 to Quit or 1 to Continue: "))
    if user_input == 0:
        break
    else :
        main_functions.main_menu()
        user_input = int(input("Please Make Selection:\t"))
        main_functions.switch_case(user_input)









