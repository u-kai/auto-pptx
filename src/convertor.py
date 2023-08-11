from src.slide import Slide
from pptx.util import Pt
from pptx.enum.text import MSO_AUTO_SIZE


class SlideConvertor:
    def __init__(self, pptx_slide_api):
        self.pptx_slide_api = pptx_slide_api
        return

    def convert(self, slide: Slide):
        for textbox in slide.textboxs:
            converted_box = self.pptx_slide_api.shapes.add_textbox(
                Pt(textbox.start_point.left),
                Pt(textbox.start_point.top),
                Pt(textbox.size.width),
                Pt(textbox.size.height),
            )
            text_frame = converted_box.text_frame
            text_frame.text = ""
            for i, text in enumerate(textbox.value.texts):
                paragraph = text_frame.add_paragraph()
                paragraph.text = text.str()
                paragraph.font.bold = text.bold
                paragraph.font.size = Pt(text.size())
            text_frame.auto_size = MSO_AUTO_SIZE.SHAPE_TO_FIT_TEXT
        return
