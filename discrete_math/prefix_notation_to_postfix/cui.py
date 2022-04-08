from core import *


def start():
    print("Enter an expression in prefix notation:")
    s = input()
    res = " ".join(solve(str_to_symbols(s)))
    print(f"Your expression in postfix notation:\n {res}")


if __name__ == "__main__":
    start()
