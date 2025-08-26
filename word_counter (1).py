# Python program to count words in a text file

def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()  # Read entire file content
            words = text.split()  # Split by whitespace into words
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None

# Example usage:
filename = r"/Users/vihangeechhatravala/Downloads/sample.txt"
count = count_words_in_file(filename)

if count is not None:
    print(f"Total number of words in '{filename}': {count}")
