import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

book_path = sys.argv[1]

from stats import word_count
from stats import char_count
from stats import sort_count

def get_book_text(file_path):
	with open(file_path) as f:
		book_contents = f.read()
	return book_contents

def main():
	monster = get_book_text(book_path)
	result = word_count(monster)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(result)
	print("--------- Character Count -------")
	characters = char_count(monster)
	characters_list = sort_count(characters)
	for item in characters_list:
		if item["char"].isalpha():
			print(f"{item['char']}: {item['num']}")	

main()

