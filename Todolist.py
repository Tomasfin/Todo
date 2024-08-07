
task_dict = {}
completed_task_dict = {}
index = 0
index2 = 0
def add_task(task_name):
    global index
    task_dict[index] = task_name
    index += 1
    
def complete_task(task_number):
    global task_dict, index2
    if task_number in task_dict:
        
        item_to_move = task_dict[task_number]
        value = task_dict.pop(task_number)
        completed_task_dict[index2] = value
        index2 += 1
        print("Task completed")
        removed_dict = {}
        for num, task in task_dict.items():
            if num >= task_number:
                removed_dict[num-1] = task
            else:
                removed_dict[num] = task
        task_dict = removed_dict
           

        
print("Welcome to your todo list.")
print("Your todo list is currently empty")
input1 = ""
while input1 != "Y" or "N":
 input1 = input("Do you want to add a task? (Y/N)\n")
 if input1.upper() == "Y":
    while True:
        input2 = input("Please enter a task:\n")
        add_task(input2)
        available_actions = "Available actions: \n Enter corresponding number to complete task \n Enter 'add' to add another task \n Enter 'view' to see all incomplete tasks \n Enter 'viewcom' to view all complete tasks"
        print(available_actions)
        while True:
            action = input("Choose an action: ")
            if action == 'add':
                break
            elif action.isdigit():
                if int(action) in task_dict:
                    complete_task(int(action))
                else:
                    print("Please ensure inputted number corresponds to a task")
            elif action == 'view':
                print("Your current tasks are:")
                if task_dict != {}:
                 for task in task_dict.items():
                    print(task)
                else:
                    print("Your todo list is empty!")
                    
            elif action == 'viewcom':
                if completed_task_dict != {}:
                 for task in completed_task_dict:
                    print(task)
                else:
                   print("You haven't completed any tasks") 

            else:
                print('Please double check your input and try again')          
            

 if input1.upper() == "N":
    print("Exiting todo list, have a good day!")
    break
 else:
    print("Please enter Y/N")


    

