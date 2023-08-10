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
        self._tops = [RecText(text)]

    def add_siblings(self,text:Text):
        self._tops.append(RecText(text))
        return


    def lists(self):
        return self._tops

    def top(self,index:int):
        if index >= len(self.lists()):
            return None
        return self.lists()[index]

    def add_child_to(self,index:int,child:Text):
        self.top(index).add_child(child)
    
    def __eq__(self,other)->bool:
        return self.lists() == other.lists() and self._child == other._child
    

class RecText():

    def __init__(self,text:Text):
        self.text = text
        self._children = []

    def add_child(self,text:Text):
        self._children.append(RecText(text))

    def child(self,index:int):
        if index >= len(self._children):
            return None
        return self._children[index]

    def str(self)->str:
        return self.text.str()

    def __eq__(self,other):
        return self.text == other.text and self._children == other._children
