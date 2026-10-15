"""Safe introductory file-handling examples."""

from pathlib import Path

DATA_FILE = Path("sample_notes.txt")


def main():
    # Write mode creates a file or replaces its old contents.
    DATA_FILE.write_text(
        "Python is useful for data science.\n"
        "Python is also used in AI and machine learning.\n",
        encoding="utf-8",
    )

    # Read all contents.
    content = DATA_FILE.read_text(encoding="utf-8")
    print("File contents:")
    print(content)

    # Read lines and search for a word.
    lines = content.splitlines()
    search_word = "Python"
    found_lines = [
        index for index, line in enumerate(lines, start=1)
        if search_word.lower() in line.lower()
    ]
    if found_lines:
        print(f"'{search_word}' found on line(s): {found_lines}")
    else:
        print(f"'{search_word}' was not found.")

    # Append adds content at the end.
    with DATA_FILE.open("a", encoding="utf-8") as file:
        file.write("This line was appended.\n")

    print("\nAfter appending:")
    print(DATA_FILE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
