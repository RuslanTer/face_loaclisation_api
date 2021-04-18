from fastapi import APIRouter, File, Form, UploadFile
from starlette.responses import Response
from validator import User_Pydantic, UserIn_Pydantic, Image_Pydantic
from models import Users, Image, Faces
from face_recognition import find_face

router = APIRouter(
    prefix="",
    tags=["all"],
    responses={404: {"description": "Not found"}},
)


@router.get("/user")
async def get_user(username: str, password: str):
    user = await Users.get(username=username)
    if user.password_hash != password:
        return {"message": "Wrong password"}
    else:
        return await User_Pydantic.from_tortoise_orm(user)


@router.post("/user/")
async def create_user(user_in: UserIn_Pydantic):
    user = await Users.create(**user_in.dict())
    user_serialized = await User_Pydantic.from_tortoise_orm(user)
    return user_serialized


@router.delete("/user")
async def delete_user(username: str, password: str):
    user = await Users.get(username=username)
    if user.password_hash != password:
        return {"message": "Wrong password"}
    else:
        return await user.delete()


@router.post("/face/image")
async def upload_image(username: str, password: str, file: bytes = File(...)):
    user = await Users.get(username=username)
    if user.password_hash != password:
        return {"message": "Wrong password"}
    faces = find_face(file)
    image = await Image.create(
        image=file,
        description='test',
        user=user,
        stats='todo stats',
        count_faces=len(faces)
    )
    faces = find_face(file)
    for face in faces:
        await Faces.create(
            box=str(face['box']),
            confidence=face['confidence'],
            left_eye=str(face['keypoints']['left_eye']),
            right_eye=str(face['keypoints']['right_eye']),
            nose=str(face['keypoints']['nose']),
            mouth_left=str(face['keypoints']['mouth_left']),
            mouth_right=str(face['keypoints']['mouth_right']),
            image=image
        )

    return await Image_Pydantic.from_tortoise_orm(image)


@router.get("/face/get-image")
async def get_image(user: UserIn_Pydantic):
    return {"message": "Hello World"}


@router.get("/face/get-faces")
async def get_faces(user: UserIn_Pydantic):
    return {"message": "Hello World"}


@router.get("/face/get-stats")
async def get_all(user: UserIn_Pydantic):
    return {"message": "Hello World"}
