import unittest

from src.convertors.slide import PlaceHolderConvertor
from src.placeholders import PlaceHolder
from src.components import Text
from tests.convertors.slide_tests import MockTitlePlaceHolder, MockContntPlaceHolder


class TestPlaceHolderConvertor(unittest.TestCase):
    def test_ListContentを変換する際はtext_frameのparagraphへのみ変換する(self):
        list_content = PlaceHolder.list_content()

        list_content.add(Text("Root1"))
        list_content.add(Text("Root2"))

        mock = MockContntPlaceHolder(2)
        sut = PlaceHolderConvertor([MockTitlePlaceHolder(), mock])
        sut.convert([list_content])

        self.assertEqual(mock.text_frame.text, "")
        self.assertEqual(mock.text_frame.paragraphs[0].text, "Root1")
        self.assertEqual(mock.text_frame.paragraphs[1].text, "Root2")

    def test_複数の兄弟を持つListContentを変換できる(self):
        list_content = PlaceHolder.list_content()

        list_content.add(Text("Root1"))
        list_content.add(Text("Root2"))
        list_content.add(Text("Root3"))

        list_content.add_child_to(0, Text("Parent1"))
        list_content.add_child_to(1, Text("Parent2"))
        list_content.add_child_to(2, Text("Parent3"))

        list_content.top(0).child(0).add_child(Text("Child1"))
        list_content.top(1).child(0).add_child(Text("Child2"))
        list_content.top(2).child(0).add_child(Text("Child3"))

        mock = MockContntPlaceHolder(2)
        sut = PlaceHolderConvertor([MockTitlePlaceHolder(), mock])
        sut.convert([list_content])

        self.assertEqual(mock.text_frame.paragraphs[0].text, "Root1")
        self.assertEqual(mock.text_frame.paragraphs[0].level, 0)
        self.assertEqual(mock.text_frame.paragraphs[1].text, "Parent1")
        self.assertEqual(mock.text_frame.paragraphs[1].level, 1)
        self.assertEqual(mock.text_frame.paragraphs[2].text, "Child1")
        self.assertEqual(mock.text_frame.paragraphs[2].level, 2)
        self.assertEqual(mock.text_frame.paragraphs[3].text, "Root2")
        self.assertEqual(mock.text_frame.paragraphs[3].level, 0)
        self.assertEqual(mock.text_frame.paragraphs[4].text, "Parent2")
        self.assertEqual(mock.text_frame.paragraphs[4].level, 1)
        self.assertEqual(mock.text_frame.paragraphs[5].text, "Child2")
        self.assertEqual(mock.text_frame.paragraphs[5].level, 2)
        self.assertEqual(mock.text_frame.paragraphs[6].text, "Root3")
        self.assertEqual(mock.text_frame.paragraphs[6].level, 0)
        self.assertEqual(mock.text_frame.paragraphs[7].text, "Parent3")
        self.assertEqual(mock.text_frame.paragraphs[7].level, 1)
        self.assertEqual(mock.text_frame.paragraphs[8].text, "Child3")
        self.assertEqual(mock.text_frame.paragraphs[8].level, 2)
