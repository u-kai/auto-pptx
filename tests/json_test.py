import unittest
import json
from src.json import slide_from_json
from src.components import Text, ListText, Font
from src.placeholders import PlaceHolder
from src.slide import Slide, Size, StartPoint


class TestJsonConvertor(unittest.TestCase):
    def test_jsonからslideを取得できる(self):
        json_str = """
        {
            "type":"title_only",
            "title":"Title",
            "list_text":{
                "top":100,
                "left":200,
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
        expected_list.top(1).child(0).add_child(child3)

        expected_placeholder = PlaceHolder.title("Title")

        expected = Slide.title_only()
        expected.add_list_text(StartPoint(200, 100), Size(0, 0), expected_list)
        expected.add_placeholder(expected_placeholder)

        self.assertEqual(sut.template, expected.template)
