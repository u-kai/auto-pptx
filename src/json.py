from dataclasses import dataclass
from src.slide import SlideType, Component, Slide
import json


def slide_from_json(json_str: str) -> Slide:
    dict = json.loads(json_str)
    return Slide.from_type(get_type(dict))


def get_type(json_dict: dict) -> SlideType:
    type = json_dict["type"]
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
