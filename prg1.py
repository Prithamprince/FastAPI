from typing import List,Dict
from datetime import date
from pydantic import BaseModel
def main(user_id:str):
    return user_id
class User(BaseModel):
    id:int
    name:str
    joined:date
