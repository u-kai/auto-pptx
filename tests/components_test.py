import unittest
from src.components import TextBox, Text, Font, FontSize, ListText


class TestText(unittest.TestCase):
    def test_textは文字列を保持して返すことできる(self):

        sut = Text("Hello World")

        self.assertEqual(sut.str(), "Hello World")

    def test_textはfontの情報を保持できる(self):

        sut = Text("Hello World")
        sut.change_font(Font.meiryo_ui())

        self.assertEqual(sut.font, Font.meiryo_ui())

    def test_textはsizeの情報を保持できる(self):

        sut = Text("Hello World")

        self.assertEqual(sut.size, FontSize(18))

        sut.change_size(FontSize(28))

        self.assertEqual(sut.size, FontSize(28))

    def test_textはboldにすることができる(self):

        sut = Text("Hello World")

        sut.to_bold()

        self.assertTrue(sut.bold)


class TestTextBox(unittest.TestCase):
    def test_複数のTextを保持可能(self):
        box = TextBox()
        box.add(Text("Hello World"))
        box.add(Text("Good Bye"))

        self.assertEqual(box.texts[0].str(), "Hello World")
        self.assertEqual(box.texts[1].str(), "Good Bye")


class TestListText(unittest.TestCase):
    def test_ListTextは再帰的な階層構造を持つ(self):
        sut = ListText(Text("Parent"))

        sut.add_child_to(0, Text("Child"))

        self.assertEqual(sut.top(0).str(), "Parent")
        self.assertEqual(sut.top(0).child(0).str(), "Child")
        self.assertEqual(sut.top(0).child(0).child(0), None)

    def test_ListTextの要素は兄弟を持つ(self):

        sut = ListText(Text("Parent1"))

        sut.add_siblings(Text("Parent2"))

        self.assertEqual(sut.top(0).str(), "Parent1")
        self.assertEqual(sut.top(1).str(), "Parent2")

    def test_ListTextの兄弟要素は子供を持つことができる(self):

        sut = ListText(Text("Parent1"))

        sut.add_siblings(Text("Parent2"))

        sut.add_child_to(1, Text("Child2"))

        self.assertEqual(sut.top(0).child(0), None)
        self.assertEqual(sut.top(1).child(0).str(), "Child2")


if __name__ == "__main__":
    unittest.main()
