
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
