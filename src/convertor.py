from src.slide import Slide


class SlideConvertor:
    def __init__(self, pptx_slide_api):
        self.pptx_slide_api = pptx_slide_api
        return

    def convert(self, slide: Slide):
        for textbox in slide.textboxs:
            converted_box = self.pptx_slide_api.shapes.add_textbox(
                textbox.start_point.left,
                textbox.start_point.top,
                textbox.size.width,
                textbox.size.height,
            )
            text_frame = converted_box.text_frame

            for i, text in enumerate(textbox.value.texts):
                if i == 0:
                    text_frame.text = text.str()
                    text_frame.fit_text(text.font.font, text.size(), text.bold)
                    continue

                paragraph = text_frame.add_paragraph()
                paragraph.text = text.str()
                paragraph.font.bold = text.bold
                paragraph.font.size = text.size()
        return
