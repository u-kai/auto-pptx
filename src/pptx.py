from pptx import Presentation


class PPTX():
    def __init__(self,filename:str):
        self.presentation = Presentation()
        self.filename = filename

    def save(self):
        self.presentation.save(self.filename)
        
        

