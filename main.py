def main():
    file_path = "books/frankenstein.txt"
    file_contents = read_file(file_path)
    
    print(f"--- Begin report of {file_path} ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()
    counts = count_characters(file_contents)
    for count in counts:
        print(f"The '{count["char"]}' character was found {count["num"]} times")

def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    chars = {}
    for c in text:
        lower = c.lower()
        if lower.isalpha():
            if not lower in chars:
                chars[lower] = 0
            chars[lower] += 1

    # sorting
    sorted = []
    for k in chars:
        v = chars[k]
        sorted.append({"char": k, "num": v})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

main()