"""Define a powerful function used elsewhere."""


THE_ANSWER: int = 42


def main() -> None:
    """Entrypoint of our program."""
    print(f"helpers.py: {__name__}")
    print(powerful(2,10))


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


# Idiomatic Python: having a main function
if __name__ == "__main__":
    maint()
# Typically you would not have an else statement.
# else:
    # print("helpers.py module was imported.")