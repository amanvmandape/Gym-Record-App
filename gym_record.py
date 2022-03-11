import os
import sys
import time
import datetime

usr_name = ""
pass_wrd = ""

def usr_login():
    global usr_name
    global pass_wrd

    os.system('cls')
    print(" ************** Welcome to Gym Trainer App ************** \n")
    print(" =============> Login to your Account \n")
    usr_name = input("Enter a User Name: ")
    usr_name = usr_name.lower()
    pass_wrd = input("Enter your password: ")

    if os.path.isfile(usr_name+".txt"):
        with open(usr_name+".txt") as f:
            password = f.read()
            if pass_wrd == password:
                print("\nYou have Successfully Login...")
                time.sleep(1.5)
                usr_panel()
            else:
                print("\nIncorrect Password")
                time.sleep(1.5)
    else:
        print("\nNo such account found...")
        time.sleep(1.5)

def usr_create():
    global usr_name
    global pass_wrd

    os.system('cls')
    print(" ************** Welcome to Gym Trainer App ************** \n")
    print(" =============> Create a New Account \n")
    usr_name = input("Enter a User Name: ")
    usr_name = usr_name.lower()
    pass_wrd = input("Enter your password: ")

    if os.path.isfile(usr_name+".txt"):
        print("\nUsername already Exists... Choose another username...")
        time.sleep(1.5)
    else:
        with open(usr_name+".txt", "w+") as f:
            password = f.write(pass_wrd)
            print("\nYour account was Successfully Created... Re-Login to Continue...")
            time.sleep(1.5)

def usr_panel():
    while True:
        os.system('cls')
        print(" ************** Welcome to Gym Trainer App ************** \n")
        print(" =============> Your Dashboard \n")
        print("Welcome, "+usr_name)
        print("\nWhat would you like to do?")
        print("1) Manage your Meal Data")
        print("2) Manage your Workout Data")
        print("x) Exit")
        usr_choice = input("\nEnter your choice: ")
        if usr_choice == "1":
            meal_data()
        elif usr_choice == "2":
            work_data()
            pass
        elif usr_choice.lower() == "x":
            break
        else:
            print("Invalid Choice Entered")
            time.sleep(1.5)

def meal_data():
    while True:
        os.system('cls')
        print(" ************** Welcome to Gym Trainer App ************** \n")
        print(" =============> Manage Meal Data \n")
        print("Welcome, "+usr_name)
        print("\nWhat would you like to do?")
        print("1) Add your Meal Data")
        print("2) View your Meal Data")
        print("x) Exit")
        usr_choice = input("\nEnter your choice: ")
        
        if usr_choice == "1":
            add_meal()
        elif usr_choice == "2":
            view_meal()
        elif usr_choice.lower() == "x":
            break
        else:
            print("Invalid Choice Entered")
            time.sleep(1.5)

def add_meal():
    os.system('cls')
    print(" ************** Welcome to Gym Trainer App ************** \n")
    print(" =============> Add Meal Data \n")
    meal = input("Enter what you ate: ")
    date = datetime.datetime.now()
    date = date.strftime("%c")

    with open(usr_name+"_meal.txt", "a+") as f:
        f.write(date+"\t"+meal+"\n")
        print("\nSuccessfully added your meal")
        time.sleep(1.5)

def view_meal():
    os.system('cls')
    print(" ************** Welcome to Gym Trainer App ************** \n")
    print(" =============> View Meal Data \n")
    with open(usr_name+"_meal.txt", "r") as f:
        for line in f:
            print(line)
        usr_choice = input("\n\nPress Enter Key to Continue...")

def work_data():
    while True:
        os.system('cls')
        print(" ************** Welcome to Gym Trainer App ************** \n")
        print(" =============> Manage Workout Data \n")
        print("Welcome, "+usr_name)
        print("\nWhat would you like to do?")
        print("1) Add your Workout Data")
        print("2) View your Workout Data")
        print("x) Exit")
        usr_choice = input("\nEnter your choice: ")
        
        if usr_choice == "1":
            add_work()
        elif usr_choice == "2":
            view_work()
        elif usr_choice.lower() == "x":
            break
        else:
            print("Invalid Choice Entered")
            time.sleep(1.5)

def add_work():
    os.system('cls')
    print(" ************** Welcome to Gym Trainer App ************** \n")
    print(" =============> Add Workout Data \n")
    meal = input("Enter what Exercise you did: ")
    date = datetime.datetime.now()
    date = date.strftime("%c")

    with open(usr_name+"_work.txt", "a+") as f:
        f.write(date+"\t"+meal+"\n")
        print("\nSuccessfully added your workout")
        time.sleep(1.5)

def view_work():
    os.system('cls')
    print(" ************** Welcome to Gym Trainer App ************** \n")
    print(" =============> View Meal Data \n")
    with open(usr_name+"_work.txt", "r") as f:
        for line in f:
            print(line)
        usr_choice = input("\n\nPress Enter Key to Continue...")

while True:
    os.system('cls')
    print(" ************** Welcome to Gym Trainer App ************** \n")
    print("Enter 1 to Login to your Account")
    print("Enter 2 to Create New Account")
    print("Enter x to exit")
    usr_choice = input("\nEnter your choice: ")
    if usr_choice == "1":
        usr_login()
    elif usr_choice =="2":
        usr_create()
    elif usr_choice.lower() == "x":
        sys.exit()
    else:
        print("\nInvalid Choice Entered")
        time.sleep(1.5)