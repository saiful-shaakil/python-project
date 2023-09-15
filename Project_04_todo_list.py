# Declaring a empty todo list
todo_list = []

def add_task(task):
    todo_list.append({"task": task, "completed": False})
    
def view_task():
    if not todo_list :
        return print("No task added.")
    """
    enumerate is a built-in Python function that allows you to iterate through an iterable (like a list) while keeping track of both the index (position) and the value of each element.
    In the context of the for loop, enumerate takes two arguments:
    The iterable you want to loop through (todo_list in this case).
    An optional start parameter (which is set to 1 in your code) that specifies the value of the first index.
    The enumerate function generates pairs of (index, value) for each element in the iterable, starting from the specified start value.
    In your code, the for loop uses i to represent the index and task to represent the value (a task dictionary) at each iteration.
    """
    for i, task in enumerate(todo_list, start = 1) :
        status = "Completed" if task['completed'] else "Incompleted"
        print(f"Task {i}: {task['task']} ({status})")

def mark_completed(task_num):
    if 1 <= task_num <= len(todo_list):
        todo_list[task_num - 1]["completed"] = True
        print(f"{task_num} number task marked as completed")
    
    else:
        print("Invalid task number.")

def delete_task(task_num):
    if 1 <= task_num <= len(todo_list):
        del todo_list[task_num - 1]
        print(f"{task_num} number task deleted.")
        
    else: 
        print("Invalid task number.")

while True :
    print("Menu: ")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark As Completed Task")
    print("4. Delete Task")
    print("5. Quiet")
    
    user_input = input("Enter you choice: ")
    
    if user_input == "1" :
        task = input("Enter your task: ")
        add_task(task)
    if user_input == "2" :
        print("Your task list: ")
        view_task()
    if user_input == "3" :
        task_num = int(input("Enter task number: "))
        mark_completed(task_num)
    if user_input == "4" :
        task_num = int(input("Enter task number: "))
        delete_task(task_num)
    if user_input == "5" :
        break
    