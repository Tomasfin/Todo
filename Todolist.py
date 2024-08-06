task_list = []
def add_task(task_name):
    task_list.append(task_name)
def task_view(task_list):
    count = 0
    for task in task_list:
        count += 1
        print(f'{count}: {task}')

# add_task('Eat')
# add_task('Sleep')
# add_task('Mine')
# add_task('Repeat')
# task_view(task_list)
