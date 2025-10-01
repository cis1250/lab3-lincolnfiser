#!/usr/bin/env python3

import re

# Function already provided
def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True

user_sentence = input("Enter a sentence: ")

while not is_sentence(user_sentence):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

# Remove punctuation and lowercase the sentence
clean_sentence = re.sub(r'[^\w\s]', '', user_sentence).lower()

# Split sentence into words
words_in_sentence = clean_sentence.split()

# Lists to store unique words and their frequencies
unique_words = []
frequencies = []

# Count frequencies
for word in words_in_sentence:
    if word in unique_words:
        index = unique_words.index(word)
        frequencies[index] = frequencies[index] + 1
    else:
        unique_words += [word]      # add word to the list
        frequencies += [1]          # start frequency at 1

# Print results
for i in range(len(unique_words)):
    print(unique_words[i] + ": " + str(frequencies[i]))
