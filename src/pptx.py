# This dependencies have to write for pptx module
import collections.abc
from pptx import Presentation

from src.slide import Slide
from src.convertors.slide import SlideConvertor
from src.convertors.presentation import PresentationConvertor


class PPTX:
    def __init__(self, filename: str):
        self.convertor = PresentationConvertor(Presentation())
        self.filename = filename
        self.page = 0

    def save(self):
        self.convertor.save(self.filename)

    def add_slide(self, slide: Slide):
        self.convertor.add_slide(slide)
        # self.presentation.slides.add_slide(self.presentation.slide_layouts[0])
        # convertor = SlideConvertor(self.presentation.slides[self.page])
        # convertor.convert(slide)
        self.page += 1
        return

    def page_num(self) -> int:
        return self.page
