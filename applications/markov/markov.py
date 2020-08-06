import random

# Plan - we're done if we have good pseudocode
# 1. Read the file `input.txt` and split it into two words
# already read in
# split into two words

# 2. Analyze the text, building up the dataset of which words
# can follow a word.
# Which words can follow a word? Any word that actually does
# any word at index + 1

# 3. Choose a random "start word" to begin.
# 4. Loop through

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

# split into words
split_words = words.split()

# analyze which words can follow other words
dataset = {}

for i in range(len(split_words) - 1):
    word = split_words[i]
    next_word = split_words[i + 1]

    if word not in dataset:
        dataset[word] = [next_word]
    else:
        dataset[word].append(next_word)

# Make a list of start words
# One way: loop over our split_words and put any start word into a list
# Another way: loop over the keys

start_words = []
for key in dataset.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)

word = random.choice(start_words)

sentences = [""] * 5
stopped = False
stop_signs = "?.!"

# construct 5 random sentences
for i in range(0, len(sentences)):
    stopped = False
    while not stopped:
        sentences[i] += (word + " ")

        # if it's a stop word, stop
        if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
            stopped = True

        # choose a random following word
        following_words = dataset[word]

        word = random.choice(following_words)

for sentence in sentences:
    print(sentence)
