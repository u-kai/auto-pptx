class Font:
    def __init__(self, font: str, size: int):
        self.font = font
        self.size = size

    def __DEFAULT_SIZE():
        return 18

    def meiryo():
        return Font("Meiryo", Font.__DEFAULT_SIZE())

    def calibri():
        return Font("Calibri", Font.__DEFAULT_SIZE())

    def meiryo_ui():
        return Font("Meiryo UI", Font.__DEFAULT_SIZE())

    def change_size(self, size: int):
        self.size = size

    def __eq__(self, other):
        return self.font == other.font and self.size == other.size


class Text:
    def __init__(self, text: str):
        self.text = text
        self.font = Font.calibri()
        self.bold = False
        return

    def str(self) -> str:
        return self.text

    def size(self) -> int:
        return self.font.size

    def change_font(self, font: Font):
        self.font = font
        return

    def change_size(self, size: int):
        self.font.size = size
        return

    def to_bold(self):
        self.bold = True
        return

    def __eq__(self, other) -> bool:
        return self.text == other.text and self.font == other.font


class TextBox:
    def __init__(self):
        self.texts = []

    def add(self, text: Text):
        self.texts.append(text)
        return


class ListText:
    def __init__(self, text: Text):
        self._tops = [RecText(text)]

    def add_siblings(self, text: Text):
        self._tops.append(RecText(text))
        return

    def lists(self):
        return self._tops

    def top(self, index: int):
        if index >= len(self.lists()):
            return None
        return self.lists()[index]

    def add_child_to(self, index: int, child: Text):
        self.top(index).add_child(child)

    def __eq__(self, other) -> bool:
        return self.lists() == other.lists()


class RecText:
    def __init__(self, text: Text):
        self.text = text
        self._children = []

    def add_child(self, text: Text):
        self._children.append(RecText(text))

    def bold(self):
        return self.text.bold

    def size(self):
        return self.text.size()

    def children(self):
        return self._children

    def child(self, index: int):
        if index >= len(self._children):
            return None
        return self._children[index]

    def str(self) -> str:
        return self.text.str()

    def __eq__(self, other):
        return self.text == other.text and self._children == other._children
