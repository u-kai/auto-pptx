# This dependencies have to write for pptx module
import collections.abc
from pptx import Presentation

from src.slide import Slide


class PPTX:
    def __init__(self, filename: str):
        self.presentation = Presentation()
        self.filename = filename
        self.convertor = SlideApiConvertor()
        self.page = 0

    def save(self):
        self.presentation.save(self.filename)

    def add_slide(self, slide: Slide):
        layout = self.convertor.convert(slide)
        self.page += 1
        return  # self.presentation.slides.add_slide(layout)

    def page_num(self) -> int:
        return self.page


class SlideApiConvertor:
    def __init__(self):
        return

    def convert(self, slide: Slide):
        return
