# Task Tracker CLI 

Task Tracker CLI is a command-line application for managing tasks. It allows you to add, list, update, and remove tasks directly from the terminal by storing data in a JSON file. The tool makes it easy to view tasks based on their status.

## Features

- **Add Task:** Create new tasks. 
- **Update Task:**  Modify existing tasks.  existentes.
- **Delete Task:**  Remove tasks. 
- **Mark Task:** Mark tasks as "In Progress" or "Completed." 
- **List Tasks:**  View all tasks or by status.


## Usage

### Add Task
To add the description it needs to be in quotation marks

```bash
python3 task-cli.py add "New Task Description"

```

### Update Task
To update a task you need to specify the ID
```bash
python3 task-cli.py update 2 "Uptade Task Description"

```

### Delete Task
To delete a task you need to specify the ID
```bash
python3 task-cli.py delete 2

```

### Mark Task Status
To be able to mark the statuses of a task you need to specify the ID.

You can mark the statuses as:
- **in progress:**  ```mark-in-progress```
- **done:** ``` mark-done```

```bash
python3 task-cli.py mark-done 5

```


### List Tasks
You can list the tasks as:
You can mark the statuses as:
- **List all tasks:**  ```list```
- **List the tasks done** ``` list-done```
- **List all tasks to do** ``` list-todo```

```bash
python3 task-cli.py list

```


### Project Link
For more details about this project, visit the [Task Tracker Project Roadmap](https://roadmap.sh/projects/task-tracker)






 
