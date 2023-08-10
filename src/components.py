class Font():
    def __init__(self,font:str):
        self.font = font

    def meiryo():
        return Font("Meiryo")

    def meiryo_ui():
        return Font("Meiryo UI")

    def __eq__(self,other):
        return self.font == other.font

class FontSize():


    def __init__(self,size:int):
        self.size = size

    def default():
        DEFAULT_SIZE = 18
        return FontSize(DEFAULT_SIZE)

    def __eq__(self,other):
        return self.size == other.size

class Text():
    def __init__(self,text:str):
        self.text = text
        self.font = Font.meiryo()
        self.size = FontSize.default()
        return 

    def str(self):
        return self.text

    def change_font(self,font:Font):
        self.font = font

    def change_size(self,size:FontSize):
        self.size = size

class TextBox():
    def __init__(self):
        self.texts = []

    def add(self,text:Text):
        self.texts.append(text) 
        return 

class ListTextBox():

    def __init__(self):
        self.texts = []

    def add(self,text:Text):
        self.texts.append(text) 
        return 
