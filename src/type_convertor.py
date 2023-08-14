from typing import Optional, List
from abc import ABCMeta, abstractmethod
from src.components import RecText
from src.slide import Slide, SlideType, Component
from src.placeholders import ListContentPlaceHolder, TitlePlaceHolder


class RecTextConvertorInterface(ABCMeta):
    @abstractmethod
    def get_text(self) -> Optional[str]:
        pass

    @abstractmethod
    def get_bold(self) -> Optional[bool]:
        pass

    @abstractmethod
    def get_size(self) -> Optional[int]:
        pass

    @abstractmethod
    def get_font(self) -> Optional[str]:
        pass

    @abstractmethod
    def get_children(self) -> Optional[List[RecText]]:
        pass


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

    def get_start_point(self) -> (Optional[int], Optional[int]):
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
