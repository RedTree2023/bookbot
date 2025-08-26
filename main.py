from stats import word_count
from stats import char_count
from stats import sort_count

def get_book_text(file_path):
	with open(file_path) as f:
		book_contents = f.read()
	return book_contents

def main():
	monster = get_book_text("books/frankenstein.txt")
	result = word_count(monster)
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(result)
	print("--------- Character Count -------")
	characters = char_count(monster)
	characters_list = sort_count(characters)
	for item in characters_list:
		if item["char"].isalpha():
			print(f"{item['char']}: {item['num']}")	

main()

