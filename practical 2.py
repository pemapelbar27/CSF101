'''def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters
def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")
def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")
from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")
def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

# Run the analysis
analyze_text('sample.txt')'''

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def count_unique_words(content):
    return len(set(content.lower().split()))

def find_longest_word(content):
    return max(content.split(), key=len)

def count_specific_word(content, word):
    return content.lower().split().count(word.lower())

def percentage_words_above_avg_length(content):
    words = content.split()
    avg_length = sum(len(word) for word in words) / len(words)
    return (sum(1 for word in words if len(word) > avg_length) / len(words)) * 100

def analyze_text(filename):
    content = read_file(filename)
    line_count = content.count('\n') + 1  # Store in a variable first

    print(f"File: {filename}")
    print(f"Lines: {line_count}")  # Use variable instead of inline expression
    print(f"Words: {len(content.split())}")
    print(f"Unique words: {count_unique_words(content)}")
    print(f"Longest word: '{find_longest_word(content)}'")
    print(f"Word 'the' appears: {count_specific_word(content, 'the')} times")
    print(f"Words longer than average: {percentage_words_above_avg_length(content):.2f}%")


# analyze_text('sample.txt')