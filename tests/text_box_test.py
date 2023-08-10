import unittest
from src.components import TextBox,Text


class TestTextBox(unittest.TestCase):
    def test_複数のTextを保持可能(self):
        box = TextBox()
        box.add(Text("Hello World"))
        box.add(Text("Good Bye"))

        self.assertEqual(box.texts[0].str(),"Hello World")
        self.assertEqual(box.texts[1].str(),"Good Bye")

        

    #def test_fontの種類を選択可能(self):
    #    sut = TextBox()
    #   s
