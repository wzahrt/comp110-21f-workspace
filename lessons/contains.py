"""Example of writing a function to process a list."""


def main() -> None:
    """Entrypoint of program."""
    names: list[str] = ["Will", "Sam", "Priya", "Mom", "Dad"]
    print(contains("sam", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True iff needle is found in haystack."""
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1

    return False


if __name__ == "__main__":
    main()
