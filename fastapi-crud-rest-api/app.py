from cgitb import text
from tkinter.font import BOLD
from typing import Optional
from wsgiref.util import request_uri
from fastapi import FastAPI, HTTPException
from datetime import datetime
from pydantic import BaseModel
from typing import Text
from uuid import uuid4 as uuid

app = FastAPI()

posts=[]

class Post(BaseModel):
    id: Optional[str]
    title:str
    autor: Optional[str]
    content:Text
    created_at:datetime=datetime.now()
    published_at: datetime
    published: bool


@app.get('/')
def read_root():
    return{"welcome":"welcom to my api"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post:Post):
    #print(post.dict())
    post.id=str(uuid())
    posts.append(post.dict())
    return posts[-1]

@app.get('/posts/{post_id}')
def get_post(post_id:str):
    for post in posts:
        if post["id"]==post_id:
            return post

    #print(post_id)
    #return "not found"
    raise HTTPException(status_code=404, detail="Post Not Found")
    #
@app.delete('/posts/{post_id}')
def delete_post(post_id:str):
    for index, post in enumerate(posts):
        if post["id"]== post_id:
            posts.pop(index)

        #print(posts)
        #print(index)
            return{"message":"Post a sido eliminado"}

    raise HTTPException(status_code=404, detail="Post Not Found")
    
@app.put('/posts/{post_id}')
def update_post(post_id:str, updatePost: Post):
    for index, post in enumerate(posts):
        if post["id"]== post_id:
            posts[index]["title"] = updatePost.title
            posts[index]["co ntent"] = updatePost.content
            posts[index]["autor"] = updatePost.autor
            return {"message":"Post a sido actualizado exitosamente"}
    raise HTTPException(status_code=404, detail="Post Not Found")
    
print("Esta es la vercion Feature-ARB")