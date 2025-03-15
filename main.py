from stats import count_words, sort_characters


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
    #file_contents = get_book_text("books/frankenstein.txt")
    #print(file_contents)
    #count_words("books/frankenstein.txt")
    #sort_characters("books/frankenstein.txt")
    report("books/frankenstein.txt")

main()