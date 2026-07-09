from fastapi import FastAPI

app = FastAPI(title="Student Management API",description="A simple REST API for student management built with FASTAPI",version="1.0.0")

@app.get("/")
def root():
    return {"massage":"Student Management API is running"}