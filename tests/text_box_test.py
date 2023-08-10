import unittest
from src.components import TextBox,Text,Font,FontSize,ListTextBox



class TextText(unittest.TestCase):
    def test_textは文字列を保持して返すことできる(self):

        sut = Text("Hello World")

        self.assertEqual(sut.str(),"Hello World")

    def test_textはfontの情報を保持できる(self):

        sut = Text("Hello World")
        sut.change_font(Font.meiryo_ui())

        self.assertEqual(sut.font,Font.meiryo_ui())

    def test_textはsizeの情報を保持できる(self):

        sut = Text("Hello World")

        self.assertEqual(sut.size,FontSize(18))

        sut.change_size(FontSize(28))

        self.assertEqual(sut.size,FontSize(28))
        



class TestTextBox(unittest.TestCase):
    def test_複数のTextを保持可能(self):
        box = TextBox()
        box.add(Text("Hello World"))
        box.add(Text("Good Bye"))

        self.assertEqual(box.texts[0].str(),"Hello World")
        self.assertEqual(box.texts[1].str(),"Good Bye")

        

class TestListTextBox(unittest.TestCase):

    def test_複数のTextを保持可能(self):
        box = ListTextBox()
        box.add(Text("Hello World"))
        box.add(Text("Good Bye"))

        self.assertEqual(box.texts[0].str(),"Hello World")
        self.assertEqual(box.texts[1].str(),"Good Bye")




if __name__ == "__main__":
    unittest.main()
