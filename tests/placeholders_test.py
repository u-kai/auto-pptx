import unittest
from src.placeholders import PlaceHolder, PlaceHolderType


class TestPlaceHolder(unittest.TestCase):
    def test_title_placeholderはtitleを保持できる(self):
        sut = PlaceHolder.title("Title")
        self.assertEqual(sut.value, "Title")
        self.assertEqual(sut.type, PlaceHolderType.TITLE)

    def test_object_placeholderは複数の文字列を保持できる(self):
        sut = PlaceHolder.object()
        sut.add("Hello World")
        sut.add("Hello Python")
        self.assertEqual(sut.value, ["Hello World", "Hello Python"])
        self.assertEqual(sut.type, PlaceHolderType.OBJECT)
