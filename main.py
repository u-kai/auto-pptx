from src.pptx import PPTX
from src.slide import Slide, StartPoint, Size
from src.components import TextBox, Text, ListText
from src.placeholders import PlaceHolder


def main_line(text: str):
    text = Text(text)
    text.change_size(28)
    text.to_bold()
    return text


def main():
    filename = "hello.pptx"
    p = PPTX(filename)
    title_slide = Slide.title_slide()
    title_slide.add_placeholder(PlaceHolder.title("Hello World"))
    p.add_slide(title_slide)

    list_content = PlaceHolder.list_content()
    memory_safe = main_line("Memory Safe")
    so_fast = main_line("Rust is so fast")
    so_safe = main_line("Rust is so safe")
    so_loved = main_line("I love Rust")
    list_content.add(memory_safe)
    list_content.add(so_fast)
    list_content.add(so_safe)
    list_content.add(so_loved)

    because_fast = Text("Because Rust has not GC")

    list_content.top(1).add_child(because_fast)

    because_love = Text("I Love Rust")
    list_content.top(3).add_child(because_love)
    list_content.top(3).child(0).add_child(because_love)

    title_and_content_slide = Slide.title_and_content()
    title_and_content_slide.add_placeholder(
        PlaceHolder.title("Rust is Very Fast and Very Safe and Very LOVED language")
    )
    title_and_content_slide.add_placeholder(list_content)
    p.add_slide(title_and_content_slide)

    p.save()


if __name__ == "__main__":
    main()
