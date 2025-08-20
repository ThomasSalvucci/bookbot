import sys
from stats import (
    get_num_words,
    get_characters_count,
    split_dictionnaries,
)


name_string = "name"
count_string = "count"
    
    
def main():    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    file_path = f"./{sys.argv[1]}"
    text = get_book_text(file_path)
    num_words = get_num_words(text)    
    characters_count = get_characters_count(text)
    split_dictionnary = split_dictionnaries(characters_count, name_string, count_string)    
    print_report(file_path, num_words, split_dictionnary)
    
    
def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
        return file_content

    
def print_report(file_path, num_words, sorted_list):    
    print("============ BOOKBOT ============")    
    print(f"Analyzing book found at {file_path[2:]}...")
    
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    
    for entry in sorted_list:
        if entry[name_string].isalpha:
            print(f"{entry[name_string]}: {entry[count_string]}") 
    
    print("============= END ===============")
    
    
main()

        