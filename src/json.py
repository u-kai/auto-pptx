from src.slide import SlideType, Component, Slide, Size, Component, StartPoint
from src.components import TextBox, ListText, Text, Font, RecText
from src.placeholders import TitlePlaceHolder, ListContentPlaceHolder
import json
from src.type_convertor import (
    RecTextConvertorInterface,
    SlideConvertorInterface,
    TextSource,
)
from typing import Optional, List


class JsonToSlideConvertor(SlideConvertorInterface):
    def __init__(self, json_str: str):
        self.dict = json.loads(json_str)
        return

    def get_type(self) -> SlideType:
        type = self.dict.get("type", None)
        return type

    def get_title(self) -> Optional[str]:
        return self.dict.get("title", None)

    def get_contents(self) -> Optional[ListContentPlaceHolder]:
        maybe_contents = self.dict.get("contents", None)
        if maybe_contents is None or len(maybe_contents) == 0:
            return None

        list_content_placeholder = ListContentPlaceHolder()
        list_content_placeholder.value = make_list_text(maybe_contents)
        return list_content_placeholder

    def get_list_texts(self) -> Optional[List[Component]]:
        maybe_list_texts = self.dict.get("list_texts", None)
        result = []
        if maybe_list_texts is None:
            return result

        for list_text_dict in maybe_list_texts:
            size = __get_size(list_text_dict)
            start_point = __get_start_point(list_text_dict)
            list_text = __get_list_text(list_text_dict)
            result.append(Component(start_point, size, list_text))

        return result


def slide_from_json(json_str: str) -> Slide:
    dict = json.loads(json_str)
    slide = Slide.from_type(__get_type(dict))

    title_placeholder = __get_title_placeholder(dict)
    if title_placeholder is not None:
        slide.add_placeholder(title_placeholder)

    list_content_placeholder = __get_list_content_placeholder(dict)
    if list_content_placeholder is not None:
        slide.add_placeholder(list_content_placeholder)

    list_texts_components = __get_list_texts_component(dict)

    for list_texts_component in list_texts_components:
        slide.add_list_text(
            list_texts_component.start_point,
            list_texts_component.size,
            list_texts_component.value,
        )

    return slide


def __get_list_content_placeholder(json_dict: dict) -> ListContentPlaceHolder:
    maybe_contents = json_dict.get("contents", None)
    if maybe_contents is None or len(maybe_contents) == 0:
        return None

    list_content_placeholder = ListContentPlaceHolder()
    list_content_placeholder.value = make_list_text(maybe_contents)
    return list_content_placeholder


def __get_list_texts_component(json_dict: dict) -> [Component]:
    maybe_list_texts = json_dict.get("list_texts", None)
    result = []
    if maybe_list_texts is None:
        return result

    for list_text_dict in maybe_list_texts:
        size = __get_size(list_text_dict)
        start_point = __get_start_point(list_text_dict)
        list_text = __get_list_text(list_text_dict)
        result.append(Component(start_point, size, list_text))

    return result


def __get_list_text(json_dict: dict) -> ListText:
    maybe_texts = json_dict.get("texts", None)
    if maybe_texts is None or len(maybe_texts) == 0:
        return None

    return make_list_text(maybe_texts)


class JsonToRecTextConvertor(RecTextConvertorInterface):
    def __init__(self, text_dict: dict):
        self.text_dict = text_dict

    def get_text_source(self):
        return TextSource(
            self.text_dict.get("text", None),
            self.text_dict.get("bold", None),
            self.text_dict.get("font", None),
            self.text_dict.get("size", None),
        )

    def get_children(self) -> Optional[List[TextSource]]:
        maybe_children = self.text_dict.get("children", None)
        if maybe_children is None:
            return None
        for child in maybe_children:
            result.add_rec_child(__get_text(child))

        return result


def make_list_text(texts_dict: [dict]) -> ListText:
    list_text = None
    for text in texts_dict:
        sibling = __get_text(text)
        if sibling is None:
            continue

        if list_text is None:
            list_text = ListText.from_rec_text(sibling)
            continue

        list_text.add_rec_siblings(sibling)

    return list_text


def __get_text(json_dict: dict) -> RecText:
    maybe_text = json_dict.get("text", None)
    if maybe_text is None:
        maybe_text = ""
    text = Text(maybe_text)
    if json_dict.get("bold", None) is not None and json_dict.get("bold", None):
        text.to_bold()
    if json_dict.get("font", None) is not None:
        font = Font.from_str(json_dict.get("font", None))
        if json_dict.get("size", None) is not None:
            font.change_size(int(json_dict.get("size", None)))
        text.change_font(font)

    result = RecText(text)

    maybe_children = json_dict.get("children", None)
    if maybe_children is None:
        return result

    for child in maybe_children:
        result.add_rec_child(__get_text(child))

    return result


def __get_start_point(json_dict: dict) -> StartPoint:
    maybe_left = json_dict.get("left", None)
    maybe_top = json_dict.get("top", None)
    if maybe_left is None and maybe_top is None:
        return StartPoint(0, 0)
    if maybe_left is None:
        return StartPoint(0, maybe_top)
    if maybe_top is None:
        return StartPoint(maybe_left, 0)
    return StartPoint(maybe_left, maybe_top)


def __get_size(json_dict: dict) -> Size:
    maybe_width = json_dict.get("width", None)
    maybe_height = json_dict.get("hegiht", None)
    if maybe_width is None and maybe_height is None:
        return Size(0, 0)

    if maybe_width is None:
        return Size(maybe_height, maybe_height)
    if maybe_height is None:
        return Size(maybe_width, maybe_width)
    return Size(maybe_width, maybe_height)


def __get_title_placeholder(json_dict: dict) -> TitlePlaceHolder:
    maybe_title = json_dict.get("title", None)
    if maybe_title is None:
        return None
    return TitlePlaceHolder(maybe_title)


def __get_type(json_dict: dict) -> SlideType:
    type = json_dict.get("type", None)
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
