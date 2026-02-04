from pydantic import BaseModel
class MyStudent(BaseModel):
    id:int
    name:str
    is_active:bool


myStd = {
    "id":123,
    "name":"Amrinder singh",
    "is_active":True
}
obj = MyStudent(**myStd)
print(obj)