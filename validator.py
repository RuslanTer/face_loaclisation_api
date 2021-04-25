from models import Users, Image, Faces
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
Image_Pydantic = pydantic_model_creator(Image, name="Image")
Faces_Pydantic_List = pydantic_queryset_creator(Faces)
Faces_Pydantic = pydantic_model_creator(Faces)