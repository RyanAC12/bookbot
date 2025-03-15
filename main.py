from stats import count_words, sort_characters
import sys


def report(filepath):
    word_count = count_words(filepath)
    char_count = sort_characters(filepath)
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {filepath}...\n")
    print(f"----------- Word Count ----------\nFound {word_count} total words")
    print("--------- Character Count -------")
    for item in char_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        report(sys.argv[1])

main()