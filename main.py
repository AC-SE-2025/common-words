import csv
import time

filename = "4000-most-common-english-words.csv"

# Load word list from CSV file into a list
def load_word_list(file_path):
    word_list = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            word_list.extend(row)  # Assuming each row contains a list of words
    return word_list

# Function 1: Check words using a linear search
def check_words_linear(word_list, text):
    words_in_text = text.split()
    found_words = []
    for word in words_in_text:
        if word in word_list:  # Linear search through the list
            found_words.append(word)
    return found_words

# Function 2: Check words using a set lookup (set)
def check_words_set(word_list, text):
    word_set = set(word_list)  # Convert list to set for faster lookup
    words_in_text = text.split()
    found_words = []
    for word in words_in_text:
        if word in word_set:  # Lookup in the set
            found_words.append(word)
    return found_words

# Function 3: Use a hash value
def check_words_hash(word_list, text):
    pass

# Timing function to compare the performance of both approaches
def time_check_functions(word_list, text):
    start_time = time.time()
    found_words_linear = check_words_linear(word_list, text)
    linear_time = time.time() - start_time

    start_time = time.time()
    found_words_set = check_words_set(word_list, text)
    set_time = time.time() - start_time

    start_time = time.time()
    found_words_hash = check_words_hash(word_list, text)
    hash_time = time.time() - start_time

    print(f"Linear Search Time: {linear_time:.6f} seconds")
    print(f"Hashed Search Time: {set_time:.6f} seconds")
    print(f"Hashed Search Time: {hash_time:.6f} seconds")

    # Optional: Check if the results are consistent
    assert found_words_linear == found_words_hash, "The two methods returned different results!"

if __name__ == "__main__":
    # Load the word list from the CSV file
    word_list = load_word_list(filename)

    # Prompt the user for a string of text
    text = input("Enter a string of text: ")

    # Compare runtime of both search methods
    time_check_functions(word_list, text)
