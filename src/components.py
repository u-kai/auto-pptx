class Text():
    def __init__(self,text:str):
        self.text = text
        return 

    def str(self):
        return self.text


class TextBox():
    def __init__(self):
        self.texts = []

    def add(self,text:Text):
        self.texts.append(text) 
        return 
