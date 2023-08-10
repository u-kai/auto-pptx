import unittest
from src.pptx import PPTX


class TestPptx(unittest.TestCase):
    def test_pptxは作成可能(self):
        filename = "hello-world.pptx"
        sut = PPTX(filename)
        sut.save()
        try :
            with open(filename,"r") as f:
                data = f.read()
                print(data)
                pass
        except:
            raise Exception("File Not Created")

if __name__ == "__main__" :
    unittest.main()

    
