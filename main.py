def main():
    path = "books/frankenstein.txt"
    book_text = open_book(path)
    words_counter = count_words(book_text)
    characters_counter = count_characters(book_text)
    sorted_characters = dict_to_sorted_list(characters_counter)
#    print(book_text)
    print(f"--- Begin report of {path} ---")
    print(f'There is {words_counter} words in this book')

    for character in sorted_characters:
        if not character["character"].isalpha():
            continue
        print(f'There is {character["counter"]} ocurence of "{character["character"]}" in this book')

    print("--- END of REPORT ---")

def open_book(path):
    with open(path) as f:
        book = f.read()
    return book

def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    lowered_book  = book.lower()
    lowered_characters = list(lowered_book)
    character_dict = {}
    for character in lowered_characters:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(c):
    return c["counter"]

def dict_to_sorted_list(character_dict):
    sorted_list = []
    for char in character_dict:
        sorted_list.append({"character": char, "counter": character_dict[char]})
    sorted_list.sort(reverse = True, key=sort_on)
    return sorted_list


main()
