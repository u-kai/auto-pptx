from dataclasses import dataclass


class PlaceHolderType:
    TITLE = "title"
    OBJECT = "object"
    CHART = "chart"
    TABLE = "table"
    SLIDE_NUMBER = "slide_number"
    DATE = "date"
    FOOTER = "footer"
    HEADER = "header"
    BODY = "body"
    SUBTITLE = "subtitle"
    CONTENT = "content"
    PICTURE = "picture"
    DIAGRAM = "diagram"
    MEDIA = "media"
    SLIDE_IMAGE = "slide_image"


@dataclass
class AbstractPlaceHolder:
    value: any
    type: PlaceHolderType


@dataclass
class TitlePlaceHolder:
    value: str
    type: PlaceHolderType = PlaceHolderType.TITLE


class ObjectPlaceHolder:
    def __init__(self):
        self.value = []
        self.type = PlaceHolderType.OBJECT

    def add(self, value: str):
        self.value.append(value)


class PlaceHolder:
    def __init__(self, name: str, placeholder_type: PlaceHolderType):
        self.name = name
        self.placeholder_type = placeholder_type

    def title(title: str) -> TitlePlaceHolder:
        return TitlePlaceHolder(title)

    def object() -> ObjectPlaceHolder:
        return ObjectPlaceHolder()
