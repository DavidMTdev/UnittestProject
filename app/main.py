from fastapi import FastAPI
from app.routers import articles

app = FastAPI()

app.include_router(articles.router, prefix="/articles", tags=["Articles"])

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Hello Bigger Applications!"}

