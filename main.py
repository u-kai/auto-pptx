from src.pptx import PPTX


def main():

    filename = "hello.pptx"
    p = PPTX(filename)
    p.save()


if __name__ == "__main__":
    main()
