from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active:bool =True

user_data ={
    'id':1,
    'username':'zara',
    'email':'zara@gmail.com',
}


invalid_user_data ={
    'id':'one',
    'username':'zara',
    'email':'zara@gmail.com',
}

try:
    user = User(**invalid_user_data)
except Exception as error:
    print("Error of data",error)

# user=User(**invalid_user_data)
# print(user)
# print(user.is_active)
#
