def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
        print(f"Found {num_words} total words")

def count_characters(path):
    char_count= {}
    with open(path) as f:
        file_contents = f.read().lower()
        for char in file_contents:
            if char in char_count and char.isalpha():
                char_count[char] += 1
            elif char.isalpha():
                char_count[char] = 1
            else:
                pass
    return char_count

def sorted_characters(path):
    char_count = count_characters(path)
    sorted_char_count = (sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    for char, char_total in sorted_char_count:
        print(f"{char}: {char_total}")
    