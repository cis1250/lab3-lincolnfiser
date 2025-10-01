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
clean_sentence = re.sub(r'[^\w\s]', '', user_sentence).lower()  #This is what I used to remove the punctuation and lower case

# Split sentence into words
words_in_sentence = clean_sentence.split() #this takes the string and seprates it into a list of words

# Lists to store unique words and their frequencies
unique_words = [] #These are both empty lists where the counts will be stored
frequencies = []

# Count frequencies
for word in words_in_sentence:  #This starts a loop for the variable(words_in_sentence)
    if word in unique_words:   #checks if word has already been seen
        index = unique_words.index(word) # finds the position/index of that word in the unique_words list.
        frequencies[index] = frequencies[index] + 1 #Increases the count of that word by 1
    else:
        unique_words += [word]      # add word to the list
        frequencies += [1]          # start frequency at 1

# Print results
for i in range(len(unique_words)):
    print(unique_words[i] + ": " + str(frequencies[i]))
