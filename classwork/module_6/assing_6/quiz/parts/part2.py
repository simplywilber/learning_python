def word_frequency(words):
    frequency = {}
    words = words.lower().split()
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def print_word_frequency(frequency):
    for word, freq in frequency.items():
        print(word, freq)

# Sample input
input_words = "hey Hi Mark hi mark"

# Get word frequency
frequency = word_frequency(input_words)

# Output
print_word_frequency(frequency)