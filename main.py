from stats import word_count
from stats import character_count
from stats import sort_character_list

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()
    
def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    num_words = word_count(book_text)
    characters_dict = character_count(book_text)
    characters_list_sorted = sort_character_list(characters_dict)

    print(F"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")

    for character in characters_list_sorted:
        letter = list(character.keys())[0]
        count = list(character.values())[0]
        if letter.isalpha():
            print(f"{letter}: {count}")

main()
