from fastapi import FastAPI
from routes import router as face
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

TORTOISE_ORM = {
    "connections": {
        "default": 'postgres://__test_app_core:__test_app_core@localhost:5432/__test_app_core'
    },
    "apps": {
        "models": {
            "models": ['aerich.models', 'models'],
            "default_connection": "default",
        }
    },
}

register_tortoise(
    app,
    TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(face)