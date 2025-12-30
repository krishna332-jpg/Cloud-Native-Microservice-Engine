from fastapi import FastAPI

app = FastAPI(title="IBM_Cloud_Ready_API")

@app.get("/")
def read_root():
    return {
        "Project": "Cloud-Native Microservice",
        "Status": "Online",
        "Environment": "Python 3.14"
    }

@app.get("/health")
def health_check():
    return {"status": "all systems go"}