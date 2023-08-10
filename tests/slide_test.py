import unittest
from src.slide import Slide,StartPoint,Size
from src.components import TextBox

class TestSlide():

    def test_slideにtext_boxを追加可能(self):

        sut = Slide()
        box = TextBox()
        box.add(Text("Hello World"))
        letf = 0
        top = 0
        point = StartPoint(left,top) 
        width = 300
        height = 300
        size = Size(width,height) 

        sut.add_textbox(point,size,box)

        self.assertEqual(sut.textboxs[0].point,point)
        self.assertEqual(sut.textboxs[0].size,size)
        self.assertEqual(sut.textboxs[0].value,box)


if __name__ == "__main__":
    unittest.main()


