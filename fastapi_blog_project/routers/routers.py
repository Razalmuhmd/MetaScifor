# routers/routers.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import BlogPost, BlogPostSchema, CreateBlogPost, UpdateBlogPost  # Ensure correct imports

router = APIRouter()

@router.get("/posts", response_model=List[BlogPostSchema])
def get_all_posts(db: Session = Depends(get_db)):
    posts = db.query(BlogPost).order_by(BlogPost.id.desc()).all()
    return posts

@router.get("/posts/{post_id}", response_model=BlogPostSchema)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(BlogPost).filter(BlogPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@router.post("/posts", response_model=BlogPostSchema, status_code=status.HTTP_201_CREATED)
def create_post(post: CreateBlogPost, db: Session = Depends(get_db)):
    new_post = BlogPost(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.put("/posts/{post_id}", response_model=BlogPostSchema)
def update_post(post_id: int, updated_post: UpdateBlogPost, db: Session = Depends(get_db)):
    existing_post = db.query(BlogPost).filter(BlogPost.id == post_id).first()
    if not existing_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if updated_post.title:
        existing_post.title = updated_post.title
    if updated_post.content:
        existing_post.content = updated_post.content

    db.commit()
    db.refresh(existing_post)
    return existing_post

@router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    existing_post = db.query(BlogPost).filter(BlogPost.id == post_id).first()
    if not existing_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    db.delete(existing_post)
    db.commit()
    return None
