from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
from app.config.database import PyObjectId

class Article(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias='_id')
    name: str = Field()
    price: float = Field()
    type: str = Field()
    memoryCapacity: int = Field(default=None)
    memoryType: str = Field(default=None)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
