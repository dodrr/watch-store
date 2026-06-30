from pydantic import BaseModel

class ProductSchema(BaseModel):
    name: str
    brand: str
    price: int 

class OrderSchema(BaseModel):
    watch: str 
    customer: str 
    price: int 

class LoginSchema(BaseModel):
    password: str 

