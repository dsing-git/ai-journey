# word_stats.py - count how many times each word appears
# 1. The sentence we want to analyse
text = "the quick brown fox jumps over the lazy dog and the fox"

# 2. Break the sentence into a list of separate words
words = text.split()
print(words)

# 3. Start with an empty dictionary
word_counts = {}

# 4. Go through every word and count it
for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1

# 5. Show the raw dictionary
print(word_counts)

# 6. Show it in a nicer format
print("\nWord frequency:")
for word in word_counts:
    print(f"{word} appears {word_counts[word]} times")