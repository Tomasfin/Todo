
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
            
        




    

add_task('Eat')
add_task('Sleep')
add_task('Mine')
add_task('Repeat')

print(task_dict)
complete_task(2)
complete_task(1)
print("Your completed tasks are:")
for t in completed_task_dict.items():
    print(t)

