# main.py

from fastapi import FastAPI
from routers.routers import router

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Blog API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
