from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    user_type: str

class Dataset(BaseModel):
    user_id: User
    original_id: str
    type: str
    status: str
    path: str
    original_source: str
    data_created: datetime

class User_Dataset(BaseModel):
    user_id: User
    dataset_id: Dataset
    is_admin: bool
    role: str

class Project(BaseModel):
    project_name: str

class Project_User(BaseModel):
    project_id: Project
    is_admin: bool
    role: str

class Dataset_Project(BaseModel):
    project_id: Project
    dataset_id: Dataset

class Portal(BaseModel):
    portal_name: str

class Dataset_Portal(BaseModel):
    dataset_id: Dataset
    portal_id: Portal



# Test models for FastAPI
class Item(BaseModel):
    name: str
    price: float
    # is_offer: Union[bool, None] = None

