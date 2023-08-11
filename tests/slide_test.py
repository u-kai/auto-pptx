import unittest
from src.slide import Slide, StartPoint, Size
from src.convertor import SlideConvertor
from src.components import TextBox, Text, Font


class TestSlide(unittest.TestCase):
    def test_slideにtext_boxを追加可能(self):

        sut = Slide()
        box = TextBox()
        box.add(Text("Hello World"))
        left = 0
        top = 0
        point = StartPoint(left, top)
        width = 300
        height = 300
        size = Size(width, height)

        sut.add_textbox(point, size, box)

        self.assertEqual(sut.textboxs[0].start_point, point)
        self.assertEqual(sut.textboxs[0].size, size)
        self.assertEqual(sut.textboxs[0].value, box)


class MockPPTXFont:
    def __init__(self):
        self.bold = False
        self.size = 18
        return


class MockPPTXParagraph:
    def __init__(self):
        self.font = MockPPTXFont()
        self.text = ""
        return


class MockPPTXTextFrame:
    def __init__(self):
        self.default = MockPPTXParagraph()
        self.text = self.default.text
        self.font = self.default.font
        self.paragraphs = [self.default]
        return

    def add_paragraph(self):
        para = MockPPTXParagraph()
        self.paragraphs.append(para)
        return para


class MockPPTXTextBox:
    def __init__(
        self,
    ):
        self.text_frame = MockPPTXTextFrame()
        return


class MockPPTXShapesApi:
    def __init__(self):
        self.textboxs = []

    def add_textbox(self, left, top, width, height) -> MockPPTXTextBox:
        textbox = MockPPTXTextBox()
        self.textboxs.append(
            {
                "left": left,
                "top": top,
                "width": width,
                "height": height,
                "textbox": textbox,
            }
        )
        return textbox


class MockPPTXSlideApi:
    def __init__(self):
        self.shapes = MockPPTXShapesApi()
        return


class TestSlideConvertor(unittest.TestCase):
    def test_slideからtextboxを取得して変換可能(self):
        # 3rd party library mock
        mock = MockPPTXSlideApi()
        # My types
        text = Text("Hello World")
        font = Font.meiryo_ui()
        font.change_size(28)
        text.change_font(font)
        text.to_bold()

        box = TextBox()
        box.add(text)

        slide = Slide()
        slide.add_textbox(
            StartPoint(0, 0),
            Size(300, 300),
            box,
        )

        sut = SlideConvertor(mock)
        sut.convert(slide)

        self.assertEqual(mock.shapes.textboxs[0]["left"], 0)
        self.assertEqual(mock.shapes.textboxs[0]["top"], 0)
        self.assertEqual(mock.shapes.textboxs[0]["width"], 300)
        self.assertEqual(mock.shapes.textboxs[0]["height"], 300)
        self.assertEqual(
            mock.shapes.textboxs[0]["textbox"].text_frame.text, "Hello World"
        )
        self.assertEqual(mock.shapes.textboxs[0]["textbox"].text_frame.font.size, 28)
        self.assertEqual(mock.shapes.textboxs[0]["textbox"].text_frame.font.bold, True)


if __name__ == "__main__":
    unittest.main()
