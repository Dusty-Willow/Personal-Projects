import json
import employee as emp

employees = []
objectList = []
newDict = {}

def collector(dict):
    global employees, details
    employees = dict.keys()
    for key in employees:
        objectList.append(emp.Employee(dict[key]["Name"], dict[key]["Age"], dict[key]["Birth"], dict[key]["Email"]))

def listEmployees():
    global objectList
    empNum = 1
    print("\n")
    
    for object in objectList:
        print(f"-----Employee Number {str(empNum)}-----\n")
        object.toString()
        empNum += 1

def main():
    # Loads employee details from relevant file
    try:
        with open('employees.json', 'rt') as file:
            data = json.load(file)

        collector(data)
        listEmployees()
        # printDict()
    except:
        print("This file doesn't exist.")


main()