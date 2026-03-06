import json
import os

# def input_task():
#     name = input("Enter the task name: ")
#     due_date = input("Enter the due date (YYYY-MM-DD): ")
#     priority = input("Enter the priority (Low, Medium, High): ")
#     status = input("Enter the status (Not started, in progress, Completed): ")
    
    # return name, due_date, priority, status
def add_task(name, due_date, priority, status):
    new_id = max([task['id'] for task in task_list], default=0) + 1
    task = {
        'id': new_id,
        'name': name,
        'due_date': due_date,
        'priority': priority,
        'status': status
    }
    task_list.append(task)
    
# def view_tasks():
#     if not task_list:
#         print("No tasks available.")
#         return
#     print(f"{'ID':<5} {'Name':<20} {'Due Date':<12} {'Priority':<10} {'Status':<15}")
#     print('-' * 65)
#     for task in task_list:
#         print(f"{task['id']:<5} {task['name']:<20} {task['due_date']:<12}"
#               f"{task['priority']:<10} {task['status']:<15}")
    

def mask_task_completion(task_id):
    for task in task_list:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            print(f"Task '{task['name']}' marked as completed.")
            return
    print("Task not found.")
    
def delete_task(task_id):
    global task_list
    task_list = [task for task in task_list if task['id'] != task_id]
    print(f"Task with ID {task_id} deleted.")
    
def clear_all_tasks():
    global task_list
    task_list.clear()
    print("All tasks cleared.")
  
def search_task(query):
    results = [task for task in task_list if query.lower() in task['name'].lower()]
    if not results:
        print("No tasks found matching the query.")
        return
    print(f"{'ID':<5} {'Name':<20} {'Due Date':<12} {'Priority':<10} {'Status':<15}")
    print('-' * 65)
    for task in results:
        print(f"{task['id']:<5} {task['name']:<20} {task['due_date']:<12}"
              f"{task['priority']:<10} {task['status']:<15}")
    
def sort_tasks(by= 'name'):
    if by == 'name':
        task_list.sort(key=lambda x: x['name'])
    elif by == 'due_date':
        task_list.sort(key=lambda x: x['due_date'])     
    elif by == 'priority':
        task_list.sort(key=lambda x: x['priority'])
    elif by == 'status':
        task_list.sort(key=lambda x: x['status'])
    else:
        print("Invalid sort option. please choose from 'name', 'due_date', 'priority', or 'status'.")
    
    #view_tasks()

def save_tasks_to_file(filename='task.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(task_list, file, ensure_ascii=False, indent=4)
    print(f"Saved to {filename} (JSON format).")
    

task_list = []

def load_tasks_from_file(filename='task.json'):
    global task_list
    if not os.path.exists(filename):
        task_list = [] 
        return False, "File not found"
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            task_list = json.load(file) 
        return True, "Success"
    except (json.JSONDecodeError, Exception):
        task_list = []
        return False, "Error loading file"

load_tasks_from_file()