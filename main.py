import sys
from stats import get_num_words
from stats import count_characters
from stats import sorted_characters
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    get_num_words(path)
    print("--------- Character Count -------")
    count_characters(path)
    sorted_characters(path)
    print("============= END ===============")
main()