from src.components import TextBox
from dataclasses import dataclass

@dataclass
class StartPoint:
    left:int 
    top:int

@dataclass
class Size:
    width:int 
    height:int

class Component():

    def __init__(self,point:StartPoint,size:Size,value:any):
        self.point = point
        self.size = size
        self.value = value

class Slide():

    def __init__(self):
        self.textboxs = []
        return 

    def add_textbox(self,point:StartPoint,size:Size,textbox:TextBox):
        self.textboxs.append(Component(point,size,textbox))
        return

