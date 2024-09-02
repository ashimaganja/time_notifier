from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"The timer app": "Version 1.0.1"}  