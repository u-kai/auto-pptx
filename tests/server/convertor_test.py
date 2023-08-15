import unittest
from src.server.convertor import (
    SlideRequestConvertor,
    SlideRequest,
    ContentRequest,
    PresentationRequestConvertor,
    PresentationRequest,
)
from src.components import Text, Font, ListText
from src.slide import Slide
from src.pptx import PPTX
from src.placeholders import PlaceHolder, TitlePlaceHolder, ListContentPlaceHolder


class TestPresentationConvertor(unittest.TestCase):
    def test_presentationを表現したrequestをpresentationに変換できる(self):
        req = PresentationRequest(filename="test.pptx")
        slide1 = SlideRequest()
        slide1.type = "title_only"
        slide1.title = "This is Slide 1"

        slide2 = SlideRequest()
        slide2.type = "title_and_content"
        slide2.title = "This is Slide 2"
        slide2.contents = [
            ContentRequest(text="Hello World"),
            ContentRequest(text="Good Bye"),
        ]
        req.slides = [slide1, slide2]

        sut = PresentationRequestConvertor(req)
        presentation = sut.convert()

        expected = PPTX("test.pptx")
        expected_slide1 = Slide.title_only()
        expected_slide1.add_placeholder(TitlePlaceHolder("This is Slide 1"))
        expected.add_slide(expected_slide1)

        expected_slide2 = Slide.title_and_content()
        expected_slide2.add_placeholder(TitlePlaceHolder("This is Slide 2"))
        list_content = ListContentPlaceHolder()
        list_content.add(Text("Hello World"))
        list_content.add(Text("Good Bye"))
        expected_slide2.add_placeholder(list_content)
        expected.add_slide(expected_slide2)

        self.assertEqual(presentation.filename, expected.filename)
        self.assertEqual(presentation.page_num(), 2)


class TestSlideConvertor(unittest.TestCase):
    def test_slideを表現したrequestをslideに変換できる(self):
        cls = SlideRequest()
        cls.type = "title_and_content"
        cls.title = "Title"
        cls.contents = [
            ContentRequest(
                text="Hello World",
                bold=True,
                font="Meiryo UI",
                size=28,
                children=[],
            ),
            ContentRequest(
                text="Hello Python",
                children=[
                    ContentRequest(text="Hello Java"),
                    ContentRequest(
                        text="Hello C#", children=[ContentRequest(text="Hello C")]
                    ),
                ],
            ),
        ]
        sut = SlideRequestConvertor(cls)
        slide = sut.convert()

        root = Text("Hello World")
        font = Font.meiryo_ui()
        font.change_size(28)
        root.change_font(font)
        root.bold()
        root2 = Text("Hello Python")
        child1 = Text("Hello Java")
        child2 = Text("Hello C#")
        child3 = Text("Hello C")
        expected_list = ListText(root)
        expected_list.add_siblings(root2)
        expected_list.top(1).add_child(child1)
        expected_list.top(1).add_child(child2)
        expected_list.top(1).child(1).add_child(child3)

        expected = Slide.title_and_content()
        expected_placeholder = PlaceHolder.title("Title")
        expected.add_placeholder(expected_placeholder)

        expected_placeholder = PlaceHolder.list_content()
        expected_placeholder.value = expected_list
        expected.add_placeholder(expected_placeholder)

        self.assertEqual(slide.template, expected.template)

        self.assertEqual(slide.placeholders[0].value, expected.placeholders[0].value)
        self.assertEqual(slide.placeholders[1].value, expected.placeholders[1].value)
