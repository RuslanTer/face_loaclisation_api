from models import Users, Image
from tortoise.contrib.pydantic import pydantic_model_creator


User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
Image_Pydantic = pydantic_model_creator(Image, name="Image")