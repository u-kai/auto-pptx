from src.pptx import PPTX
from src.slide import Slide, StartPoint, Size
from src.components import TextBox, Text


def main():

    filename = "hello.pptx"
    p = PPTX(filename)
    slide = Slide()

    box = TextBox()
    text = Text("Hello World")
    text.to_bold()
    text.change_size(28)
    box.add(text)

    text = Text("Good Bye")
    box.add(text)

    slide.add_textbox(StartPoint(50, 50), Size(30, 30), box)

    box = TextBox()
    text = Text("Rust Good Language")
    text.to_bold()
    text.change_size(28)
    box.add(text)

    text = Text("Python Good Language.But I love Rust more than Python")
    box.add(text)

    slide.add_textbox(StartPoint(150, 150), Size(100, 500), box)

    p.add_slide(slide)
    p.save()


if __name__ == "__main__":
    main()
