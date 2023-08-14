from fastapi import FastAPI
from pydantic import BaseModel


class ListContentPlaceHolderData(BaseModel):
    lists: [str]


class WriteTitlePageData(BaseModel):
    title: str
    sub_title: str | None


def listen():
    app = FastAPI()
    # listen to post requests
    # with json data
    # and return a json response
    @app.post("/api")
    async def root():

        return {"message": "Hello World"}
