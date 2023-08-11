from src.pptx import PPTX
from src.slide import Slide, StartPoint, Size
from src.components import TextBox, Text


def main():

    filename = "hello.pptx"
    p = PPTX(filename)
    slide = Slide()

    box = TextBox()
    text = Text("Hello World")
    box.add(text)

    slide.add_textbox(StartPoint(0, 0), Size(300, 300), box)

    p.add_slide(slide)
    p.save()


if __name__ == "__main__":
    main()
