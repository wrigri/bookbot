def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contents(book_path)
    word_count = get_word_count(book_contents)
    char_count_d = get_char_count_dict(book_contents)
    char_list = get_sorted_char_list(char_count_d)
    print_report(book_path, word_count, char_list)


def print_report(book_path, word_count, char_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for entry in char_list:
        print(f"The '{entry[1]}' character was found {entry[0]} times")
    print("--- End report ---")

def get_sorted_char_list(char_dict):
    char_list = []
    for k, v in char_dict.items():
        if k.isalpha():
            char_entry = (v, k)
            char_list.append(char_entry)

    char_list.sort(reverse=True)         
    return char_list

    

def get_word_count(book_contents):
    words = book_contents.split()
    return len(words)


def get_char_count_dict(book_contents):
    lower_contents = book_contents.lower()
    char_count = {}
    for c in lower_contents:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count


def get_book_contents(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

main()