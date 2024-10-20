"""
Word Occurrences
Estimate: 20 minutes
Actual:   28 minutes
"""
text = input("Text: ")
words = text.split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

longest_word_length = max(len(word) for word in word_counts.keys())

for word, count in sorted(word_counts.items()):
    print(f"{word:{longest_word_length}} : {count}")