from src.components import TextBox, ListText
from dataclasses import dataclass


@dataclass
class StartPoint:
    left: int
    top: int


@dataclass
class Size:
    width: int
    height: int


class Component:
    def __init__(self, start_point: StartPoint, size: Size, value: any):
        self.start_point = start_point
        self.size = size
        self.value = value


class Slide:
    def __init__(self):
        self.textboxs: [Component] = []
        self.list_texts: [Component] = []
        return

    def add_textbox(self, point: StartPoint, size: Size, textbox: TextBox):
        self.textboxs.append(Component(point, size, textbox))
        return

    def add_list_text(self, point: StartPoint, size: Size, list_text: ListText):
        self.list_texts.append(Component(point, size, list_text))
        return
