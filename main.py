from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    user_type: str

class User_Dataset(BaseModel):
    user_id: User
    is_admin: bool
    role: str

class Project(BaseModel):
    # project_id: str
    project_name: str

class Project_User(BaseModel):
    project_id: Project
    is_admin: bool
    role: str


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}