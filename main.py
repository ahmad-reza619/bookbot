def main():
    text = get_book_text("books/frankenstein.txt")
    words_len = get_book_words_len(text)
    print(f"The book has {words_len} words.")
    get_book_char_count(text)

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents

def get_book_words_len(contents):
    words = contents.split()
    return len(words)

def get_book_char_count(contents):
    dict = {}
    for c in contents:
        char = c.lower()
        if char == " " or char == "\n":
            continue
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    for k, v in dict.items():
        print(f"character {k} occurs {v} times")


main()
