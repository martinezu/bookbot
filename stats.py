def count_words(book):
    counter = 0
    for word in book.split():
        counter += 1
    print(f"{counter} words found in the document")
    return counter


def sort_by(item):
    return item["quant"]

def count_characters(book):
    book = book.lower()
    char_list = [{"char": "a", "quant": book.count("a")}, {"char": "b", "quant": book.count("b")},{"char": "c", "quant": book.count("c")},
                 {"char": "d", "quant": book.count("d")},{"char": "e", "quant": book.count("e")},{"char": "f", "quant": book.count("f")},
                 {"char": "g", "quant": book.count("g")},{"char": "h", "quant": book.count("h")},{"char": "i", "quant": book.count("i")},
                 {"char": "j", "quant": book.count("j")},{"char": "k", "quant": book.count("k")},{"char": "l", "quant": book.count("l")},
                 {"char": "m", "quant": book.count("m")},{"char": "n", "quant": book.count("n")},{"char": "o", "quant": book.count("o")},
                 {"char": "p", "quant": book.count("p")},{"char": "q", "quant": book.count("q")},{"char": "r", "quant": book.count("r")},
                 {"char": "s", "quant": book.count("s")},{"char": "t", "quant": book.count("t")},{"char": "u", "quant": book.count("u")},
                 {"char": "v", "quant": book.count("v")},{"char": "w", "quant": book.count("w")},{"char": "x", "quant": book.count("x")},
                 {"char": "y", "quant": book.count("y")},{"char": "z", "quant": book.count("z")}
                 ]
    char_list.sort(reverse=True,key=sort_by)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words")
    print("--------- Character Count -------")
    for character in char_list:
        print(f"{character["char"]}: {character["quant"]}")
    print("============= END ===============")