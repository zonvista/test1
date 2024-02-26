tasks=[]
def listOfTask():
    print("the list of tasks are:")
    if (len(tasks)==0):
        print("No tasks are available")
    for num in range(len(tasks)):
        print(f"{num}. "+ tasks[num])

def addTask():
    task =input("Enter the list which u want to add: ")
    tasks.append(task)
    print("Sucessfully Added")

def deleteTask():  
    listOfTask()
    delete=int(input("Enter the task number which u want to delete: "))
    tasks.pop(delete)
    print("Sucessfully Deleted ")

while(True):
    print("Welcome to to-do List App :) ")
    print("-------------------------")
    print("1. List of Tasks")
    print("2. Add a new Task")
    print("3. Delete a Task")
    print("4. Quit ")
    choose=int(input("Choose an option: "))
    if (choose == 1):
        listOfTask()
    elif (choose == 2):
        addTask()
    elif (choose == 3):
        deleteTask()
    elif (choose == 4):
        print("Thank you")
        break
    else:
        print("Invalid Input")  
       

