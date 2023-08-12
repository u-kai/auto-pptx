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
    placeholder = PlaceHolder.content()
    placeholder.add("Hello World")
    placeholder.add("Hello Python")
    title_and_content_slide.add_placeholder(placeholder)
    placeholder = PlaceHolder.title("Hello")
    title_and_content_slide.add_placeholder(placeholder)
    p.add_slide(title_and_content_slide)

    title_and_content_slide = Slide.title_and_content()
    placeholder = PlaceHolder.list_content()

    placeholder.add(Text("Root"))
    text = Text("Parent")
    text.to_bold()
    text.change_size(40)
    placeholder.add_child_to(0, text)
    placeholder.top(0).child(0).add_child(Text("Child"))
    title_and_content_slide.add_placeholder(placeholder)
    p.add_slide(title_and_content_slide)

    p.save()


if __name__ == "__main__":
    main()
