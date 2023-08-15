from typing import Optional, List
from abc import ABCMeta, abstractmethod
from src.components import RecText, Text, Font
from src.slide import Slide, SlideType, Component
from src.placeholders import ListContentPlaceHolder, TitlePlaceHolder
from dataclasses import dataclass


class SlideConvertorInterface(metaclass=ABCMeta):
    def convert(self) -> Slide:
        slide = Slide.from_type(str_to_type(self.get_type()))

        if self.get_title() is not None:
            slide.add_placeholder(TitlePlaceHolder(self.get_title()))

        list_content_placeholder = self.get_contents()
        if list_content_placeholder is not None:
            slide.add_placeholder(list_content_placeholder)

        list_texts_components = self.get_list_texts()

        for list_texts_component in list_texts_components:
            slide.add_list_text(
                list_texts_component.start_point,
                list_texts_component.size,
                list_texts_component.value,
            )

        return slide

    @abstractmethod
    def get_title(self) -> Optional[str]:
        pass

    @abstractmethod
    def get_type(self) -> Optional[str]:
        pass

    @abstractmethod
    def get_contents(self) -> Optional[ListContentPlaceHolder]:
        pass

    @abstractmethod
    def get_list_texts(self) -> Optional[List[Component]]:
        pass


@dataclass
class TextSource:
    text: Optional[str]
    bold: Optional[bool]
    size: Optional[int]
    font: Optional[str]


class RecTextConvertorInterface(metaclass=ABCMeta):
    def convert(self) -> RecText:
        source = self.get_text_source()
        if source.text is None:
            source.text = ""
        text = Text(source.text)
        if source.bold is not None and source.bold:
            text.to_bold()
        if source.font is not None:
            font = Font.from_str(source.font)
            if source.size is not None:
                font.change_size(source.size)
            text.change_font(font)

        result = RecText(text)

        maybe_children = self.get_children()
        if maybe_children is None:
            return result

        for child in maybe_children:
            result.add_rec_child(__get_text(child))

        return result

    @abstractmethod
    def get_text_source(self) -> Optional[TextSource]:
        pass

    @abstractmethod
    def get_children(self) -> Optional[List[TextSource]]:
        pass


def str_to_type(type: Optional[str]) -> SlideType:
    if type is None:
        return SlideType.BLANK
    if type == "title_only":
        return SlideType.TITLE_ONLY
    if type == "title_and_content":
        return SlideType.TITLE_AND_CONTENT
    if type == "blank":
        return SlideType.BLANK
    if type == "title_slide":
        return SlideType.TITLE_SLIDE
    if type == "section_header":
        return SlideType.SECTION_HEADER
    if type == "two_content":
        return SlideType.TWO_CONTENT
    if type == "comparison":
        return SlideType.COMPARISON
    if type == "content_with_caption":
        return SlideType.CONTENT_WITH_CAPTION
    if type == "picture_with_caption":
        return SlideType.PICTURE_WITH_CAPTION
