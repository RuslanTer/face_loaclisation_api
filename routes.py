from fastapi import APIRouter, File, Form, UploadFile
from starlette.responses import Response
from validator import User_Pydantic, UserIn_Pydantic, Image_Pydantic, Faces_Pydantic_List, Faces_Pydantic
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
    faces_for_del = []
    for face in faces:
        if face['confidence']<0.97:
            faces_for_del.append(face)
    for face_del in faces_for_del:
        faces.remove(face_del)
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
async def get_image(username: str, password: str, image_id: int):
    image = await Image.get(id=image_id)
    result = await Image_Pydantic.from_tortoise_orm(image)
    response = {'stats':result, 'image':str(image.image)}
    return response

@router.get("/face/get-faces")
async def get_faces(username: str, password: str, image_id: int):
    image = await Image.get(id=image_id)
    faces = await Faces.filter(image=image)
    print(type(faces), '_____________________________')
    response = [await Faces_Pydantic.from_tortoise_orm(face) for face in faces]
    return response


@router.get("/face/get-stats")
async def get_all(username: str, password: str):
    user = await Users.get(username=username)
    if user.password_hash != password:
        return {"message": "Wrong password"}
    images = await Image.filter(user=user)
    response = [await Image_Pydantic.from_tortoise_orm(iamge) for iamge in images]
    return response
