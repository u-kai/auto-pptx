import unittest
from src.slide import Slide, StartPoint, Size
from src.components import TextBox, Text, ListText


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

    def test_slideにlist_textを追加可能(self):
        sut = Slide()
        list_text = ListText(Text("Root"))
        list_text.add_child_to(0, Text("Parent"))
        list_text.top(0).child(0).add_child(Text("Child"))
        left = 0
        top = 0
        point = StartPoint(left, top)
        width = 300
        height = 300
        size = Size(width, height)

        sut.add_list_text(point, size, list_text)

        self.assertEqual(sut.list_texts[0].start_point, point)
        self.assertEqual(sut.list_texts[0].size, size)
        self.assertEqual(sut.list_texts[0].value, list_text)


if __name__ == "__main__":
    unittest.main()
