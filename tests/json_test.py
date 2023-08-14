import unittest
from src.json import slide_from_json, JsonToSlideConvertor
from src.components import Text, ListText, Font
from src.placeholders import PlaceHolder
from src.slide import Slide, Size, StartPoint


class TestJsonConvertor(unittest.TestCase):
    def test_jsonからlist_content_slideを取得できる(self):
        json_str = """
        {
            "type":"list_content",
            "title":"Title",
            "contents":[
                {
                    "text":"Hello World",
                    "bold":true,
                    "font":"Meiryo UI",
                    "size":28
                },
                {
                    "text":"Hello Python",
                    "children":[
                        {
                            "text":"Hello Java"
                        },
                        {
                            "text":"Hello C#",
                            "children":[
                                {
                                    "text":"Hello C"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        """

        sut = slide_from_json(json_str)

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

        self.assertEqual(sut.placeholders[0], expected.placeholders[0])
        self.assertEqual(sut.placeholders[1].value, expected.placeholders[1].value)

        sut = JsonToSlideConvertor(json_str)
        sut = sut.convert()
        self.assertEqual(sut.placeholders[0], expected.placeholders[0])
        self.assertEqual(sut.placeholders[1].value, expected.placeholders[1].value)

    def test_jsonからtitle_slideを取得できる(self):
        json_str = """
        {
            "type":"title_only",
            "title":"Title",
            "list_texts": [
                {
                    "top":100,
                    "left":200,
                    "width":300,
                    "height":400,
                    "texts":[
                        {
                            "text":"Hello World",
                            "bold":true,
                            "font":"Meiryo UI",
                            "size":28
                        },
                        {
                            "text":"Hello Python",
                            "children":[
                                {
                                    "text":"Hello Java"
                                },
                                {
                                    "text":"Hello C#",
                                    "children":[
                                        {
                                            "text":"Hello C"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        """

        sut = slide_from_json(json_str)

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

        expected_placeholder = PlaceHolder.title("Title")

        expected = Slide.title_only()
        expected.add_list_text(StartPoint(200, 100), Size(300, 400), expected_list)
        expected.add_placeholder(expected_placeholder)

        self.assertEqual(sut.template, expected.template)
        self.assertEqual(sut.placeholders, expected.placeholders)
        self.assertEqual(sut.list_texts[0].value, expected.list_texts[0].value)
