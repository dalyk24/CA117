#!/usr/bin/env python3

import sys

# Create list of words, and variable to count word A letters shared by word B
words = sys.stdin.read().strip().split()
chars2match = words[0]

# Loop through word A letter by letter in reverse order
for char in words[0][::-1]:
    # Store last letter in word B shared by word A and its position in word B
    cross = words[1].rfind(char)
    if cross != -1:
        last_char = char
        break

# Loop through word A letter by letter
for char in words[0]:
    # If current letter matches last shared letter in word B and is last instance of
    # letter in word A, print word B horizontally and skip to next letter
    if last_char == char and chars2match.count(last_char) == 1:
        print(words[1])
        continue
    # If current letter is in word A but isn't last instance of it, remove this
    # instance of letter from running count
    elif char in chars2match:
        chars2match = chars2match.replace(char, "", 1)

    # Print current letter of word A padded with "." characters, so word A prints
    # vertically and crosses horizontally printed word B at last shared letter
    print("." * cross + char + "." * (len(words[1]) - cross - 1))
