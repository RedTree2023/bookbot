def word_count(text):
        word_count = 0
        book = text
        words = text.split()
        for word in words:
                word_count += 1
        return (f"Found {word_count} total words")

def char_count(book_text):
        book_text = book_text.lower()
        counts = {}
        for char in book_text:
                if char in counts:
                        counts[char] += 1
                else:
                        counts[char] = 1
        return counts
        
def sort_count(counts):
        char_list = []
        for char, count in counts.items():
                char_list.append({"char" : char, "num" : count})
        def sort_on(item):
                return item["num"]
        char_list.sort(reverse=True, key=sort_on)
        return char_list