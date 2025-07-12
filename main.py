from stats import *

def main():
    path = "books/frankenstein.txt"
    book_text = open_book(path)
    words_counter = count_words(book_text)
    characters_counter = count_characters(book_text)
    sorted_characters = dict_to_sorted_list(characters_counter)
    print(f"--- Begin report of {path} ---")
    print(f'{words_counter} words found in the document')

    for character in sorted_characters:
        if not character["character"].isalpha():
            continue
        print(f'There is {character["counter"]} ocurence of "{character["character"]}" in this book')

    print("--- END of REPORT ---")


main()
