'''A To-Do List application is a useful project that helps users manage and organize
 their tasks efficiently. This project aims to create a command-line or GUI-based application 
 using Python, allowing users to create, update, and track their to-do lists.'''

#print ("Welcome to a To-Do List Application")
x = "Welcome to a To-Do List Application"
print (x.center(170, " "))


    
def adder(): 
    while True:
        i = input ("Do you want to add task? (Y/N)")         
        if i.upper() == "Y":
            t = input("Enter the task: ")
            l.append(t)            
        else:
            printer()            
            break

def creator():
    global l     
    l = []
    adder()


def printer ():
    print("\nYour current list is as follows: ")
    for index, item in enumerate(l, start=1):
        print(f"{index}. {item}")
    '''for item in l:
        print(f"* {item}")'''
    
def updater():
    print("\nWhich element would you like to replace")
    printer()
    indt = int(input("Enter the element number you wish to replace: "))
    l.pop(indt-1)
    a = input("Enter the new task you wish to add: ")
    l.insert(indt-2, a)
    printer()

def task_deleter(): #define this function
    print("\nWhich element would you like to delete")
    printer()
    indt = int(input("Enter the element number you wish to delete: "))
    l.pop(indt-1)
    printer()

def deleter():
    print ("Are you sure you want to delete this list? (y/n)")
    choice = input("")
    if choice == 'y':
        l.clear()
        printer()
    elif choice == 'n':
        pass
   


#main code
    
while True:
    print ("\n-----------------------------------------------\n")
    print(f"\nHey !!!\nChoose an option?\na. Create a new list\nb. Modify pre-existing list\nc. Delete a list\nd. Show the List\nPress any other key to quit the program")
    choice = input("")
    repeat = ''
    if choice.upper()=="A":
        creator()
        print("\nList successfully created")
        
    elif choice.upper()=="B":

        while True:
            print(f"\nWhich type of modify you want to do?\na. Add a task\nb. change a task\nc. Delete a task\nPress 'z' to go back to the previous menu\nPress any other key to quit the program")
            choice = input("")
            repeat = ''
            if choice.upper()=="A":                                
                if l != None:
                    printer()
                    adder()
                    
                else:
                    print ("Pls create a new list first!")
                print("\nYou have successfully Modified")

            elif choice.upper()=="B":
                updater()
                print("\nYou have successfully updated")
                
            elif choice.upper()=="C":
                task_deleter()
                
                print("\nYou have successfully Deleted a task")

            elif choice.upper()=='Z':
                break   
                
            else: 
                print("\nPlease select any 1 out of the given options")
                print ("-------------------THANKYOU----------------------------\n")
                break
        break   
        
    elif choice.upper()=="C":
        deleter()
        print("\nYou have deleted a list")
    
    elif choice.upper()=="D":
        printer()

    else: 
        print ("-------------------THANKYOU----------------------------\n")
        break