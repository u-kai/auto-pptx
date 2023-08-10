import unittest
from src.pptx import PPTX
from src.slide import Slide #,Size,StartPoint,TextBox
import os



class TestPptx(unittest.TestCase):

    def test_pptxはスライド０でも作成可能(self):
        filename = "hello-world.pptx"
        sut = PPTX(filename)
        sut.save()
        try :
            with open(filename,"r") as f:
                print("Success Create File")
        except Exception as e:
            print(e)
            raise Exception("File Not Created")
        finally:
            os.remove(filename) 

    def test_pptxにslideを追加可能(self):
        filename = "hello-world.pptx"
        sut = PPTX(filename)
        slide = Slide()

        sut.add_slide(slide)

        self.assertEqual(slide.page_num(), 1)





if __name__ == "__main__" :
    unittest.main()

