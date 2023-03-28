"""
Word Occurrences.
Estimate: 25 min
Actual: 19 min
"""

word_to_count = {}
text = input("Enter text: ")
words = text.split()
max_len = max(len(word) for word in words)
for word in words:
    if word in word_to_count.keys():
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

for word, count in word_to_count.items():
    print(f"{word:{max_len}}: {count}")
