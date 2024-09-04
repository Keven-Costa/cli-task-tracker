import json
import sys
from datetime import datetime

arguments = sys.argv
method = arguments[1]
descripton = arguments[len(arguments) - 1]

    
def find_task_by_id(task_id, data):
    for task in data:
        if task['id'] == task_id:

            return task
    return None
    
def load_data():
    with open('tasks.json', 'r') as file:
        return json.load(file)

def save_data(data):
    with open('tasks.json', 'w') as file:
        json.dump(data, file, indent=4)

def getCurrentDateAndTime():
    currentDate = datetime.now()
    
    # Format date and time
    formattedDate = currentDate.strftime("%d, %B, %Y  - %H:%M:%S")
    return formattedDate

def idGenerator():
    
    data = load_data()

    if len(data) > 0:
        new_object = data[len(data) - 1] 
        value = new_object["id"] + 1
        return value
    else:
        return 1

def checkId(id):
    data = load_data()
    
    desired_value = id
    desired_key = 'id'
    
    # Scrolling through the list to find the dictionary that matches the criterion
    for new_object in data:
        if new_object.get(desired_key) == desired_value:
            return True
            break  # To stop after finding the first result
        
    print("Error: ID not found")
    return False

def checksMethod(method):
    methods = ['add', 'update', 'delete', 'mark-in-progress','mark-done',
               'list', 'list-done', 'list-todo', 'list-in-progress']
    
    if method in methods:
        return True
    else:
        print("Invalid command: " + method)
        return False
        
def add():
    data = load_data()
        
    meu_objeto ={
        "id": idGenerator(),
        "description": descripton,
        "status": "todo",
        "createdAt": getCurrentDateAndTime(),
        "updatedAt": getCurrentDateAndTime(),
            }
        
    data.append(meu_objeto)
        # Save the changes back to the JSON file
    save_data(data)
        
    if len(data) > 0:
        print(f"Task added successfully (ID: {meu_objeto.get('id')})")
    else:
        print(f"Task added successfully (ID: 1)")
           
def update(task_id):
    data = load_data()
        
    task = find_task_by_id(task_id, data)
    if task:
        task["description"] = descripton
        task["updatedAt"] = getCurrentDateAndTime()

        
        save_data(data)
        print(f"Task updated successfully (ID: {task_id})")
    else:
        print(f"Error: Task with ID {task_id} not found")
       
def delete(task_id):
    data = load_data()
    task = find_task_by_id(task_id, data)
    if task:
        data.remove(task)
        save_data(data)
        print(f"Task deleted successfully (ID: {task_id})")
    else:
        print(f"Error: Task with ID {task_id} not found")   
              
def update_task_status(task_id, new_status):
    data = load_data()
    task = find_task_by_id(task_id, data)
    
    
    if task:
        task["status"] = new_status
        task["updatedAt"] = getCurrentDateAndTime()
        save_data(data)
        print(f"Task status updated to '{new_status}' (ID: {task_id})")
    else:
        print(f"Error: Task with ID {task_id} not found")
   
def markInProgress(task_id):
    update_task_status(task_id, 'in-progress')

def markDone(task_id):
    update_task_status(task_id, 'done')
       
def listTasks():
    
    data = load_data()
    
    # Scrolling through the list to find the dictionary that matches the criterion
    for new_object in data:
        print(
            f"id : {new_object['id']}, \n"
            f"description : {new_object['description']}, \n"
            f"status : {new_object['status']}, \n"
            f"createdAt : {new_object['createdAt']}, \n"
            f"updatedAt : {new_object['updatedAt']}\n"
        )

def listTasksDone():
    
    data = load_data()
    
    # Scrolling through the list to find the dictionary that matches the criterion
    for new_object in data:
        if new_object.get('status') == 'done':
            print(
                f"id : {new_object['id']}, \n"
                f"description : {new_object['description']}, \n"
                f"status : {new_object['status']}, \n"
                f"createdAt : {new_object['createdAt']}, \n"
                f"updatedAt : {new_object['updatedAt']}\n"
            )

def listTasksTodo():
    
    data = load_data()
    
    # Scrolling through the list to find the dictionary that matches the criterion
    for new_object in data:
        if new_object.get('status') == 'todo':
            print(
                f"id : {new_object['id']}, \n"
                f"description : {new_object['description']}, \n"
                f"status : {new_object['status']}, \n"
                f"createdAt : {new_object['createdAt']}, \n"
                f"updatedAt : {new_object['updatedAt']}\n"
            )

def listTasksInProgress():
    
    data = load_data()
    
    # Scrolling through the list to find the dictionary that matches the criterion
    for new_object in data:
        if new_object.get('status') == 'in-progress':
            print(
                f"id : {new_object['id']}, \n"
                f"description : {new_object['description']}, \n"
                f"status : {new_object['status']}, \n"
                f"createdAt : {new_object['createdAt']}, \n"
                f"updatedAt : {new_object['updatedAt']}\n"
            )
    
# Adds a new task
if method == 'add':
    add()

# Updates a task
elif method == 'update':
    id = int(arguments[2])
    if checkId(id) == True:
        update(id)
        
# Delete a task      
elif method == 'delete':
    id = int(arguments[2])
    if checkId(id) == True:
        delete(id)
        
# Marks a task as: In-progress
elif method == 'mark-in-progress':
    id = int(arguments[2])
    if checkId(id) == True:
        markInProgress(id)

# Marks a task as: mark-done
elif method == 'mark-done':
    id = int(arguments[2])
    if checkId(id) == True:
        markDone(id)
        
# lists all tasks
elif method == 'list':
    listTasks()

# lists all the tasks done 
elif method == 'list-done':
    listTasksDone()
    
# List all the tasks to do
elif method == 'list-todo':
    listTasksTodo()

# List all the tasks in-progress
elif method == 'list-in-progress':
    listTasksInProgress()

# Checks if the command is invalid
elif checksMethod(method) == True:
    checksMethod(method)
