from pydantic import BaseModel
from typing import Optional, List
from src.slide import Slide, SlideType
from src.components import Text, Font, ListText, RecText
from src.placeholders import TitlePlaceHolder, ListContentPlaceHolder
from src.pptx import PPTX


class ContentRequest(BaseModel):
    text: str
    bold: Optional[bool]
    size: Optional[int]
    font: Optional[str]
    children: Optional[List["ContentRequest"]]


class SlideRequest(BaseModel):
    title: Optional[str]
    type: Optional[str]
    contents: Optional[List[ContentRequest]]


class PresentationRequest(BaseModel):
    filename: str
    slides: Optional[List[SlideRequest]]


class PresentationRequestConvertor:
    def __init__(self, req: PresentationRequest):
        self.req = req

    def convert(self) -> PPTX:
        pptx = PPTX(self.req.filename)
        for slide_req in self.req.slides:
            slide = SlideRequestConvertor(slide_req).convert()
            pptx.add_slide(slide)
        return pptx


def change_text(text: Text, req: ContentRequest):
    if req.bold is not None and req.bold:
        text.to_bold()
    if req.font is not None:
        font = Font.from_str(req.font)
        size = req.size
        if size is not None:
            font.change_size(size)
        text.change_font(font)


class SlideRequestConvertor:
    def __init__(self, req: SlideRequest):
        self.req = req

    def convert(self) -> Slide:
        slide = self.__generate_slide_from_type()
        self.__add_title_placeholder(slide)
        self.__add_list_content_placeholder(slide)
        return slide

    def __add_list_content_placeholder(self, slide):
        def make_list_text(list: List[ContentRequest]) -> ListText:
            list_text = None
            for text in list:
                sibling = __get_text(text)
                if sibling is None:
                    continue

                if list_text is None:
                    list_text = ListText.from_rec_text(sibling)
                    continue

                list_text.add_rec_siblings(sibling)

            return list_text

        def __get_text(content: ContentRequest) -> RecText:
            text = Text(content.text)
            change_text(text, content)
            result = RecText(text)

            maybe_children = content.children
            if maybe_children is None or len(maybe_children) == 0:
                return result

            for child in maybe_children:
                result.add_rec_child(__get_text(child))

            return result

        if self.req.contents is None or len(self.req.contents) == 0:
            return

        list_content_placeholder = ListContentPlaceHolder()
        list_content_placeholder.value = make_list_text(self.req.contents)
        slide.add_placeholder(list_content_placeholder)
        return

    def __add_title_placeholder(self, slide: Slide):
        if self.req.title is None:
            return

        slide.add_placeholder(TitlePlaceHolder(self.req.title))
        return

    def __generate_slide_from_type(self) -> Slide:
        return Slide.from_type(self.__generate_slide_type())

    def __generate_slide_type(self) -> SlideType:
        if self.req.type is None:
            return SlideType.BLANK
        if self.req.type == "title_only":
            return SlideType.TITLE_ONLY
        if self.req.type == "title_and_content":
            return SlideType.TITLE_AND_CONTENT
        if self.req.type == "blank":
            return SlideType.BLANK
        if self.req.type == "title_slide":
            return SlideType.TITLE_SLIDE
        if self.req.type == "section_header":
            return SlideType.SECTION_HEADER
        if self.req.type == "two_content":
            return SlideType.TWO_CONTENT
        if self.req.type == "comparison":
            return SlideType.COMPARISON
        if self.req.type == "content_with_caption":
            return SlideType.CONTENT_WITH_CAPTION
        if self.req.type == "picture_with_caption":
            return SlideType.PICTURE_WITH_CAPTION
