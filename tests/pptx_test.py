import unittest
from src.pptx import PPTX
import os

class TestPptx(unittest.TestCase):
    def test_pptxは作成可能(self):
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

if __name__ == "__main__" :
    unittest.main()

    
