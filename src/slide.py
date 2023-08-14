from src.components import TextBox, ListText
from dataclasses import dataclass
from src.placeholders import AbstractPlaceHolder


class SlideType:
    TITLE_SLIDE = "TITLE_SLIDE"
    TITLE_AND_CONTENT = "TITLE_AND_CONTENT"
    SECTION_HEADER = "SECTION_HEADER"
    TWO_CONTENT = "TWO_CONTENT"
    COMPARISON = "COMPARISON"
    TITLE_ONLY = "TITLE_ONLY"
    BLANK = "BLANK"
    CONTENT_WITH_CAPTION = "CONTENT_WITH_CAPTION"
    PICTURE_WITH_CAPTION = "PICTURE_WITH_CAPTION"


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
        self.placeholders: [AbstractPlaceHolder] = []
        self.template = SlideType.BLANK
        return

    def add_textbox(self, point: StartPoint, size: Size, textbox: TextBox):
        self.textboxs.append(Component(point, size, textbox))
        return

    def add_list_text(self, point: StartPoint, size: Size, list_text: ListText):
        self.list_texts.append(Component(point, size, list_text))
        return

    def add_placeholder(self, placeholder: AbstractPlaceHolder):
        self.placeholders.append(placeholder)
        return

    ####################### Factory Methods #######################

    def from_type(slide_type: SlideType):
        this = Slide()
        this.template = slide_type
        return this

    def title_slide():
        this = Slide()
        this.template = SlideType.TITLE_SLIDE
        return this

    def title_and_content():
        this = Slide()
        this.template = SlideType.TITLE_AND_CONTENT
        return this

    def section_header():
        this = Slide()
        this.template = SlideType.SECTION_HEADER
        return this

    def two_content():
        this = Slide()
        this.template = SlideType.TWO_CONTENT
        return this

    def comparison():
        this = Slide()
        this.template = SlideType.COMPARISON
        return this

    def title_only():
        this = Slide()
        this.template = SlideType.TITLE_ONLY
        return this

    def blank():
        this = Slide()
        this.template = SlideType.BLANK
        return this

    def content_with_caption():
        this = Slide()
        this.template = SlideType.CONTENT_WITH_CAPTION
        return this

    def picture_with_caption():
        this = Slide()
        this.template = SlideType.PICTURE_WITH_CAPTION
        return this

    ####################### other #######################

    def __eq__(self, other):
        return (
            self.template == other.template
            and self.textboxs == other.textboxs
            and self.list_texts == other.list_texts
            and self.placeholders == other.placeholders
        )
