from pydantic import BaseModel
from typing import Optional
from src.slide import Slide


class ContentRequest(BaseModel):
    text: str
    bold: Optional[bool]
    size: Optional[int]
    font: Optional[str]
    children: Optional["ContentRequest"]


class SlideRequest(BaseModel):
    title: Optional[str]
    type: Optional[str]
    contents: Optional[ContentRequest]


class SlideRequestConvertor:
    def __init__(self, req: SlideRequest):
        self.req = req

    def convert(self) -> Slide:
        return Slide()
