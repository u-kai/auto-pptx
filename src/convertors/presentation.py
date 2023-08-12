from src.slide import Slide, SlideType
from src.convertors.slide import SlideConvertor


class SlideLayoutIndex:
    TITLE_SLIDE = 0
    TITLE_AND_CONTENT = 1
    SECTION_HEADER = 2
    TWO_CONTENT = 3
    COMPARISON = 4
    TITLE_ONLY = 5
    BLANK = 6
    CONTENT_WITH_CAPTION = 7
    PICTURE_WITH_CAPTION = 8


class PresentationConvertor:
    def __init__(self, presentation):
        self.presentation = presentation

    def add_slide(self, slide: Slide):
        slide_layout = self._convert_slide_to_slide_layout(slide)
        _slide = self.presentation.slides.add_slide(slide_layout)
        slide_convertor = SlideConvertor(_slide)
        slide_convertor.convert(slide)

    def save(self, filename: str):
        self.presentation.save(filename)

    def _convert_slide_to_slide_layout(self, slide: Slide):
        if slide.template == SlideType.TITLE_SLIDE:
            return self.presentation.slide_layouts[SlideLayoutIndex.TITLE_SLIDE]

        if slide.template == SlideType.TITLE_AND_CONTENT:
            return self.presentation.slide_layouts[SlideLayoutIndex.TITLE_AND_CONTENT]

        if slide.template == SlideType.SECTION_HEADER:
            return self.presentation.slide_layouts[SlideLayoutIndex.SECTION_HEADER]

        if slide.template == SlideType.TWO_CONTENT:
            return self.presentation.slide_layouts[SlideLayoutIndex.TWO_CONTENT]

        if slide.template == SlideType.COMPARISON:
            return self.presentation.slide_layouts[SlideLayoutIndex.COMPARISON]

        if slide.template == SlideType.TITLE_ONLY:
            return self.presentation.slide_layouts[SlideLayoutIndex.TITLE_ONLY]

        if slide.template == SlideType.BLANK:
            return self.presentation.slide_layouts[SlideLayoutIndex.BLANK]

        if slide.template == SlideType.CONTENT_WITH_CAPTION:
            return self.presentation.slide_layouts[
                SlideLayoutIndex.CONTENT_WITH_CAPTION
            ]

        if slide.template == SlideType.PICTURE_WITH_CAPTION:
            return self.presentation.slide_layouts[
                SlideLayoutIndex.PICTURE_WITH_CAPTION
            ]

        raise ValueError("Invalid slide type")
