# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# SKang,2.14.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", "r")
for row in objFile:
    lstRow = row.split(",") # Returns a list!
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
    #print(dicRow)
    #print(dicRow["Task"] + "|" + dicRow["Priority"])
    print(lstTable, "<<List with Dictionary objects")
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table #Option 1
    if (strChoice.strip() == '1'):
        print("Your Current Data is: ")
        for objRow in lstTable:
            #print(lstTable["Task"] + "|" + lstTable["Priority"])
            print(objRow)
        continue

    # Step 4 - Add a new item to the list/Table  #Option 2
    elif (strChoice.strip() == '2'):
        while(True):
            print("Type in 'Task' and 'Priority' for your To-Do List")
            strTask = str(input(" Enter a Task: "))
            strPriority = str(input(" Enter Priority: "))
            lstTable.append({"Task": strTask, "Priority": strPriority})
            strChoice = input("Exit? ('y/n'):  ")
            if strChoice.lower() == 'y':
                break
        print(lstTable, "<< List with Dictionary objects")
        continue

    # Step 5 - Remove a new item from the list/Table #Option 3
    elif (strChoice.strip() == '3'):
        while(True):
            strTask = input("Item to Remove:  ")
            for objRow in lstTable:
                if objRow["Task"].lower() ==strTask.lower():
                    lstTable.remove(objRow)
                    print("Row removed!")
                    print(lstTable, "<< List with Dictionary objects")
                else:
                    print("Row not found!")
                    print(lstTable, "<< List with Dictionary objects")
            strChoice = input("Exit? ('y/n'):  ")
            if strChoice.lower() == 'y':
                break
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file  #Option 4
    elif (strChoice.strip() == '4'):
        print("Would you like to save your data?")
        saveData = str(input("Enter 'y' or 'n': "))
        if saveData == "y":
            objFile = open("ToDoList.txt", "w")
            for objRow in lstTable:
                objFile.write(str(objRow["Task"]) + "," + str(objRow["Priority"]) + "\n")
            objFile.close()
            print("Now in File!")
        else:
            print("Your data was not saved!")
            break
        continue
    # Step 7 - Exit program  #Option 5
    elif (strChoice.strip() == '5'):
        print("Exit!")
        break  # and Exit the program
