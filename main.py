def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    print(f"{count_words(text)} words found in this document\n")
    count_characters(text)
    print("--- End Report ---")

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    for c in text:
        lower = c.lower()
        if lower in chars:
            chars[lower] +=1
        else:
            chars[lower] = 1
    # print("BEFORE SORTING")
    # print(chars)
    sort_words(chars)
    return chars

def sort_words(chars):
    # print("AFTER SORTING")
    sorted_list = sorted(chars.items(), key=lambda x:x[1], reverse=True)
    for key, value in sorted_list:
        if key.isalpha():
            print(f"The {key} character was found {value} times")

def get_book_text(path):
    with open(path) as f:
        print(f"--- Begin report of {path} ---")
        return f.read()

main()
