#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_input = input("Enter a sentence: ")

words_in_sentence = sentence.split()

# Create two lists with enough space for all words
words = [""] * len(words_in_sentence)
frequencies = [0] * len(words_in_sentence)

unique_count = 0  # track how many unique words we've added

# Count word frequencies
for word in words_in_sentence:
    found = False
    for i in range(unique_count):
        if words[i] == word:
            frequencies[i] += 1
            found = True
            break
    if not found:
        words[unique_count] = word
        frequencies[unique_count] = 1
        unique_count += 1

# Print results
for i in range(unique_count):
    print(words[i], ":", frequencies[i]


