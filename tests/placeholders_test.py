import unittest
from src.placeholders import PlaceHolder, PlaceHolderType
from src.components import Text, ListText


class TestPlaceHolder(unittest.TestCase):
    def test_title_placeholderはtitleを保持できる(self):
        sut = PlaceHolder.title("Title")
        self.assertEqual(sut.value, "Title")
        self.assertEqual(sut.type, PlaceHolderType.TITLE)

    def test_list_content_placeholderは複数の階層がある文字列を保持できる(self):
        sut = PlaceHolder.list_content()
        sut.add(Text("Root"))
        sut.add_child_to(0, Text("Parent"))
        sut.top(0).child(0).add_child(Text("Child"))

        expected = ListText(Text("Root"))
        expected.add_child_to(0, Text("Parent"))
        expected.top(0).child(0).add_child(Text("Child"))

        self.assertEqual(sut.value.lists(), expected.lists())
        self.assertEqual(sut.type, PlaceHolderType.LIST_CONTENT)

    def test_object_placeholderは複数の文字列を保持できる(self):
        sut = PlaceHolder.object()
        sut.add("Hello World")
        sut.add("Hello Python")
        self.assertEqual(sut.value, ["Hello World", "Hello Python"])
        self.assertEqual(sut.type, PlaceHolderType.OBJECT)
