task_list = []
task_dict = {}
completed_task_dict = {}
def add_task(task_name):
    task_list.append(task_name)
def task_view():
    count = 0
    for task in task_list:
        count += 1
        task_dict[count] = task
    for t in task_dict.items():
        print(t)
def complete_task(task_number):
    count = 1
    if task_number in task_dict:
        item_to_move = task_dict[task_number]
        value = task_dict.pop(task_number)
        completed_task_dict[count] = value
        count += 1
        print("Task completed")

    else:
        print(f"You don't have a task {task_number}")





    

add_task('Eat')
add_task('Sleep')
add_task('Mine')
add_task('Repeat')
task_view()
complete_task(2)
