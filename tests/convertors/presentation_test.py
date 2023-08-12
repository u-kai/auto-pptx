import unittest
from src.convertors.presentation import PresentationConvertor, SlideLayoutIndex
from src.slide import Slide


class MockSlideLayout:
    def __init__(self, index):
        self.index = index


class MockSlideLayouts:
    def __init__(self):
        self.access_slide_layouts_index = []

    def __getitem__(self, index):
        self.access_slide_layouts_index.append(MockSlideLayout(index))
        return


class MockSlides:
    def __init__(self):
        self.add_slide_access = []
        self.add_slide_time = 0

    def add_slide(self, slide_layout):
        self.add_slide_time += 1
        self.add_slide_access.append(slide_layout)


class MockPresentation:
    def __init__(self):
        self.save_files = []
        self.slide_layouts = MockSlideLayouts()
        self.slides = MockSlides()

    def slide_layouts_access(self):
        return self.slide_layouts.access_slide_layouts_index

    def save(self, filename):
        self.save_files.append(filename)

    def add_slide_time(self):
        return self.slides.add_slide_time


class TestPresentationConvertor(unittest.TestCase):
    def test_新しいスライドを追加できる(self):
        mock = MockPresentation()

        sut = PresentationConvertor(mock)

        slide0 = Slide.title_only()
        slide1 = Slide.blank()
        slide2 = Slide.title_and_content()

        sut.add_slide(slide0)
        sut.add_slide(slide1)
        sut.add_slide(slide2)

        sut.save("test.pptx")

        access = mock.slide_layouts_access()
        self.assertEqual(len(access), 3)
        self.assertEqual(access[0].index, SlideLayoutIndex.TITLE_ONLY)
        self.assertEqual(access[1].index, SlideLayoutIndex.BLANK)
        self.assertEqual(access[2].index, SlideLayoutIndex.TITLE_AND_CONTENT)

        self.assertEqual(mock.add_slide_time(), 3)

        self.assertEqual(mock.save_files[0], "test.pptx")
