from typing import List
from fastapi import APIRouter, HTTPException, status, Body
from fastapi.encoders import jsonable_encoder

from app.config.database import db
from app.models.article import Article

router = APIRouter()

@router.get("/", response_description="Get all articles")
async def getAll():
    
    return [Article(**article) for article in db.articles.find()]

@router.get("/{id}", response_model=Article, response_description="Get a articles")
async def getById(id: str):
    if ItemExists(id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article {id} not found")

    return db.articles.find_one({"_id": id})

@router.post("/", response_model=Article, response_description="Add a article", status_code=status.HTTP_201_CREATED)
async def create(article: Article = Body(...)):
    article = jsonable_encoder(article)
    new_article = db.articles.insert_one(article)
    
    return db.articles.find_one({"_id": new_article.inserted_id})

@router.put("/{id}", response_description="Update a article", status_code=status.HTTP_204_NO_CONTENT)
async def update(id: str, body: Article = Body(...)):
    if ItemExists(id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article {id} not found")

    db.articles.update_one({"_id": id}, {"$set": body.dict()})

@router.delete("/{id}", response_description="Delete a article", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    if ItemExists(id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article {id} not found")
    
    db.articles.delete_one({"_id": id})


def ItemExists(id):
    return db.articles.find_one({"_id": id})
