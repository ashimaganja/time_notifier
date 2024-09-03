from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return "This is the homepage"

@app.get("/tasks")
async def task_list():
    return "This is the task list" 

@app.get("/new-task")
async def create_newtask():
    return "This is where you will create tasks"

