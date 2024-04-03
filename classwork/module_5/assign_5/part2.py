def remove_punctuation(text):
    # Define punctuation marks
    punctuation_marks = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Remove punctuation
    text_without_punctuation = ''
    for char in text:
        if char not in punctuation_marks:
            text_without_punctuation += char

    return text_without_punctuation

def word_frequency_counter(text):
    # Remove punctuation and split the text into words
    words = remove_punctuation(text).lower().split()

    # Count the frequency of each word
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

# Call the function with example text
word_freq = word_frequency_counter("This is a sample text. A text contains sample words. Words repeat in the text.")

# Print result
print(word_freq)