import unittest
from src.components import TextBox,Text,Font,FontSize,ListText



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

        

class TestListText(unittest.TestCase):
    def test_ListTextは再帰的な階層構造を持つ(self):
        sut = ListText(Text("Parent"))

        sut.add_child(Text("Child"))

        self.assertEqual(sut.lists()[0],Text("Parent"))
        self.assertEqual(sut.child(),ListText(Text("Child")))
        self.assertEqual(sut.child().lists()[0],Text("Child"))
        self.assertEqual(sut.child().child(),None)

    def test_ListTextの要素は兄弟を持つ(self):

        sut = ListText(Text("Parent1"))

        sut.add_siblings(Text("Parent2"))

        self.assertEqual(sut.lists()[0],Text("Parent1"))
        self.assertEqual(sut.lists()[1],Text("Parent2"))



if __name__ == "__main__":
    unittest.main()
