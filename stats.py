def get_num_words(file_content: str):
    words = file_content.split()
    return len(words)


def get_characters_count(file_content: str):
    lowercase_file_content = file_content.lower()
    characters_count = {}
    for character in lowercase_file_content:
        if not character in characters_count: 
            characters_count[character] = 1
        else:
            characters_count[character] += 1
    return characters_count

def split_dictionnaries(dictionnary: dict, name_string: str, count_string: str):
    split_dictionnary=[]
    for key in dictionnary:
        split = {name_string: key, count_string: dictionnary[key]}
        split_dictionnary.append(split)
    split_dictionnary.sort(reverse=True, key= lambda entry: entry[count_string])
    return split_dictionnary

