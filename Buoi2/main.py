from enum import Enum
from fastapi import FastAPI, Path, Query

app = FastAPI(
    title="Hello World",
    description="Backend API for Hello World",
    version="0.1.0"
)


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


fake_tasks_db = [
    {
        "task_id": 1,
        "title": "Học FastAPI cơ bản",
        "status": TaskStatus.pending,
    },
    {
        "task_id": 2,
        "title": "Thiết kế RESTful API",
        "status": TaskStatus.in_progress,
    },
    {
        "task_id": 3,
        "title": "Hoàn thành TaskHub API",
        "status": TaskStatus.completed,
    },
]

@app.get("/tasks/{task_id}")
async def get_task_by_id(
    task_id: int = Path(..., title="The ID of the task to get", ge=1)
):
    for task in fake_tasks_db:
        if task["task_id"] == task_id:
            return {"task": task}
    return {"error": "Task not found"}

@app.get("/tasks/")
async def get_tasks(
    status: TaskStatus | None = Query(
        None, description="Lọc theo trạng thái công việc"
    ),
    skip: int = Query(0, ge=0, description="Số lượng bản ghi bỏ qua"),
    limit: int = Query(10, ge=1, le=50, description="Số lượng bản ghi tối đa"),
):
    result = fake_tasks_db
    if status:
        result = [t for t in result if t["status"] == status]
    return {"tasks": result[skip : skip + limit]}