class Font():
    def __init__(self,font:str):
        self.font = font

    def meiryo():
        return Font("Meiryo")

    def meiryo_ui():
        return Font("Meiryo UI")

    def __eq__(self,other):
        return self.font == other.font

class Text():
    def __init__(self,text:str):
        self.text = text
        self.font = Font.meiryo()
        return 

    def str(self):
        return self.text

    def change_font(self,font:Font):
        self.font = font

class TextBox():
    def __init__(self):
        self.texts = []

    def add(self,text:Text):
        self.texts.append(text) 
        return 
