from src.pptx import PPTX
from src.slide import Slide, StartPoint, Size
from src.components import TextBox, Text, ListText


def main():

    filename = "hello.pptx"
    p = PPTX(filename)
    title_slide = Slide.title_slide()
    box = TextBox()
    text = Text("Hello World")
    text.to_bold()
    text.change_size(28)
    box.add(text)
    text = Text("Good Bye")
    box.add(text)
    title_slide.add_textbox(StartPoint(50, 50), Size(30, 30), box)

    title_and_content_slide = Slide.title_and_content()
    text = Text("Rust Good Language")
    text.to_bold()
    text.change_size(28)
    list = ListText(text)
    list.add_siblings(Text("Python Good Language.But I love Rust more than Python"))
    list.add_child_to(0, Text("C++ Good Language"))
    list.top(0).child(0).add_child(Text("C Good Language"))

    title_and_content_slide.add_list_text(StartPoint(150, 150), Size(100, 500), list)

    p.add_slide(title_slide)
    p.add_slide(title_and_content_slide)
    p.save()


if __name__ == "__main__":
    main()
