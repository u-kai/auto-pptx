import unittest
from src.server.convertor import SlideRequestConvertor, SlideRequest, ContentRequest
from src.components import Text, Font, ListText
from src.slide import Slide
from src.placeholders import PlaceHolder, TitlePlaceHolder, ListContentPlaceHolder


class TestSlideConvertor(unittest.TestCase):
    def test_slideを表現したrequestをslideに変換できる(self):
        cls = SlideRequest()
        cls.type = "list_content"
        cls.title = "Title"
        content1 = ContentRequest
        content1.text = "Hello World"
        content1.bold = True
        content1.font = "Meiryo UI"
        content1.size = 28
        content2 = ContentRequest
        content2.text = "Hello Python"
        content3 = ContentRequest
        content3.text = "Hello Java"
        content4 = ContentRequest
        content4.text = "Hello C#"
        content5 = ContentRequest
        content5.text = "Hello C"
        content2.children = [content3, content4]
        content4.children = [content5]
        cls.contents = [content1, content2]

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

        self.assertEqual(slide.placeholders[0], expected.placeholders[0])
        self.assertEqual(slide.placeholders[1].value, expected.placeholders[1].value)
