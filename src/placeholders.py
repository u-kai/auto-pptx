from dataclasses import dataclass
from src.components import Text, ListText


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
    LIST_CONTENT = "list_content"


@dataclass
class AbstractPlaceHolder:
    value: any
    type: PlaceHolderType


@dataclass
class TitlePlaceHolder:
    value: str
    type: PlaceHolderType = PlaceHolderType.TITLE


class ContentPlaceHolder:
    def __init__(self):
        self.value = []
        self.type = PlaceHolderType.CONTENT

    def add(self, value: str):
        self.value.append(value)


class ObjectPlaceHolder:
    def __init__(self):
        self.value = []
        self.type = PlaceHolderType.OBJECT

    def add(self, value: str):
        self.value.append(value)


class ListContentPlaceHolder:
    def __init__(self):
        self.value: ListText = None
        self.type = PlaceHolderType.LIST_CONTENT

    def add(self, value: Text):
        if self.value is None:
            self.value = ListText(value)
            return
        self.value.add_siblings(value)

    def add_child_to(self, index: int, value: Text):
        self.value.add_child_to(index, value)

    def top(self, index: int):
        return self.value.top(index)


class PlaceHolder:
    def __init__(self, name: str, placeholder_type: PlaceHolderType):
        self.name = name
        self.placeholder_type = placeholder_type

    def list_content() -> ListContentPlaceHolder:
        return ListContentPlaceHolder()

    def content() -> ContentPlaceHolder:
        return ContentPlaceHolder()

    def title(title: str) -> TitlePlaceHolder:
        return TitlePlaceHolder(title)

    def object() -> ObjectPlaceHolder:
        return ObjectPlaceHolder()
