# models.py

from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel, EmailStr

# SQLAlchemy model
class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    email = Column(String, index=True)

# Pydantic models
class BlogPostSchema(BaseModel):
    id: int
    title: str
    content: str
    email: EmailStr

    class Config:
        from_attributes = True  # Use this instead of orm_mode

class CreateBlogPost(BaseModel):
    title: str
    content: str
    email: EmailStr

class UpdateBlogPost(BaseModel):
    title: str = None
    content: str = None
