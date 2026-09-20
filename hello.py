"""软件工程实验 1：最小可运行程序。"""


def greeting() -> str:
    """返回程序的问候语。"""
    return "Hello, World!"


def main() -> None:
    """打印问候语。"""
    print(greeting())


if __name__ == "__main__":
    main()

