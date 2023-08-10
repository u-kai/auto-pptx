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

    def str(self)->str:
        return self.text

    def change_font(self,font:Font):
        self.font = font

    def change_size(self,size:FontSize):
        self.size = size

    def __eq__(self,other)->bool:
        return self.text == other.text and self.font == other.font and self.size == other.size



class TextBox():
    def __init__(self):
        self.texts = []

    def add(self,text:Text):
        self.texts.append(text) 
        return 


class ListText():
    def __init__(self,text:Text):
        self._tops = [text]
        self._child = None

    def add_child(self,child:Text):
        self._child = ListText(child)
        return

    def add_siblings(self,text:Text):
        self._tops.append(text)
        return

    def lists(self):
        return self._tops

    def child(self):
        return self._child

    def __eq__(self,other)->bool:
        return self.lists() == other.lists() and self._child == other._child
    
