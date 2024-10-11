from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

class Task:
    def __init__(self, task_id: int, task_title: str, task_desc: str = "", is_finished: bool = False):
        self.task_id = task_id
        self.task_title = task_title
        self.task_desc = task_desc
        self.is_finished = is_finished

# Initialize task database
task_db = [
    Task(1, "Laboratory Activity", "Create Laboratory Activity 2", False)
]

def find_task(task_id: int) -> Optional[Task]:
    return next((task for task in task_db if task.task_id == task_id), None)

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")
    return task.__dict__

@app.post("/tasks")
def create_task(task_title: str, task_desc: Optional[str] = "", is_finished: bool = False):
    task_id = len(task_db) + 1
    new_task = Task(task_id, task_title, task_desc, is_finished)
    task_db.append(new_task)
    return {"message": "New Task Successfully Created.", "task": new_task.__dict__}

@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_title: Optional[str] = None, task_desc: Optional[str] = None, is_finished: Optional[bool] = None):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")

    if task_title:
        task.task_title = task_title
    if task_desc:
        task.task_desc = task_desc
    if is_finished is not None:
        task.is_finished = is_finished

    return {"message": "Task Successfully Updated.", "task": task.__dict__}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")
    
    task_db.remove(task)
    return {"message": "Task Successfully Deleted."}

@app.put("/tasks/{task_id}")
def replace_task(task_id: int, task_title: str, task_desc: Optional[str] = "", is_finished: bool = False):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")

    task.task_title = task_title
    task.task_desc = task_desc
    task.is_finished = is_finished

    return {"message": "Task Successfully Replaced.", "task": task.__dict__}
