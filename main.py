from stats import count_words, count_characters
import sys

def get_book_text (path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    count_characters(get_book_text(sys.argv[1]))


main()