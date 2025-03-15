def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def count_words(filepath):
    file_contents = get_book_text(filepath)
    words = file_contents.split()
    counter = 0
    for word in words:
        counter += 1
    print(f"{counter} words found in the document")


def count_characters(filepath):
    char_dict = {}
    file_contents = get_book_text(filepath)
    for char in file_contents:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
    print(char_dict)