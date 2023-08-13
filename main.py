from src.pptx import PPTX
from src.slide import Slide, StartPoint, Size
from src.components import TextBox, Text, ListText
from src.placeholders import PlaceHolder


def main():
    filename = "hello.pptx"
    p = PPTX(filename)
    title_slide = Slide.title_slide()
    title_slide.add_placeholder(PlaceHolder.title("Hello World"))
    p.add_slide(title_slide)

    title_and_content_slide = Slide.title_and_content()
    title_and_content_slide.add_placeholder(
        PlaceHolder.title("Rust is Very Fast and Very Safe and Very LOVED language")
    )
    list_content = PlaceHolder.list_content()
    list_content.add(Text("Rust is memory safe"))
    text = Text("Rust is so fast")
    text.change_size(28)
    text.to_bold()
    list_content.add(text)
    text = Text("Rust is so safe")
    list_content.add(text)
    text = Text("Because Rust has not GC")
    text.to_bold()
    list_content.add_child_to(1, text)
    text = Text("I love Rust")
    list_content.add(text)
    text = Text("I love Rust")
    text.to_bold()
    list_content.add_child_to(2, text)
    list_content.value.top(2).child(0).add_child(text)
    title_and_content_slide.add_placeholder(list_content)
    p.add_slide(title_and_content_slide)

    p.save()


if __name__ == "__main__":
    main()
