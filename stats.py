def word_count(text):
    return len(text.split())

def character_count(text):
    count_dict = {}
    for character in text:
        if character.lower() not in count_dict:
            count_dict[character.lower()] = 1
        else:
            count_dict[character.lower()] += 1

    return count_dict

def sort_on(dict):
    return list(dict.values())[0]

def sort_character_list(character_dict):
    sorted_character_list = []

    for character, count in character_dict.items():
        sorted_character_list.append({character: count})

    sorted_character_list.sort(reverse=True, key=sort_on)

    return sorted_character_list
