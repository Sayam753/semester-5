"""Main script to generate posting list."""

import re
import os
import json
from collections import Counter

posting_list = dict()
vocab = dict()
with open("posting_list.json", "w") as file:
    json.dump(posting_list, file)

stop_words = ("a", "about", "above", "after", "again", "against", "ain", "all", "am", "an",
              "and", "any", "are", "aren", "aren't", "as", "at", "be", "because", "been",
              "before", "being", "below", "between", "both", "but", "by", "can", "couldn",
              "couldn't", "d", "did", "didn", "didn't", "do", "does", "doesn", "doesn't",
              "doing", "don", "don't", "down", "during", "each", "few", "for", "from",
              "further", "had", "hadn", "hadn't", "has", "hasn", "hasn't", "have", "haven",
              "haven't", "having", "he", "her", "here", "hers", "herself", "him", "himself",
              "his", "how", "i", "if", "in", "into", "is", "isn", "isn't", "it", "it's", "its",
              "itself", "just", "ll", "m", "ma", "me", "mightn", "mightn't", "more", "most", 
              "mustn", "mustn't", "my", "myself", "needn", "needn't", "no", "nor", "not", "now",
              "o", "of", "off", "on", "once", "only", "or", "other", "our", "ours", "ourselves",
              "out", "over", "own", "re", "s", "same", "shan", "shan't", "she", "she's", "should",
              "should've", "shouldn", "shouldn't", "so", "some", "such", "t", "than", "that", 
              "that'll", "the", "their", "theirs", "them", "themselves", "then", "there", "these",
              "they", "this", "those", "through", "to", "too", "under", "until", "up", "ve", "very",
              "was", "wasn", "wasn't", "we", "were", "weren", "weren't", "what", "when", "where",
              "which", "while", "who", "whom", "why", "will", "with", "won", "won't", "wouldn",
              "wouldn't", "y", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
              "yourself", "yourselves", "could", "he'd", "he'll", "he's", "here's", "how's", "i'd",
              "i'll", "i'm", "i've", "let's", "ought", "she'd", "she'll", "that's", "there's", "they'd",
              "they'll", "they're", "they've", "we'd", "we'll", "we're", "we've", "what's", "when's",
              "where's", "who's", "why's", "would")

for file_index in range(101, 282):
    with open(f"th-dataset/{file_index}.txt") as file:
        # Preprocessing
        data = file.readlines()[0].strip()
        data = re.sub(r"\d+", "", data)  # Remove digits
        data = re.sub(r"[^\w\s]", " ", data)  # Remove punctuation
        data = re.findall(r'[A-Za-z]+', data)  # Tokenize words
        data_dict = Counter(data)  # Create data dict
     
        # Removing stop words
        stop_words_in_data = set(data_dict).intersection(stop_words)
        for words in stop_words_in_data:
            del data_dict[words]
    
    # Update the posting list
    with open("posting_list.json", "r") as file:
        posting_list = json.load(file)
        # Merging the dictionaries
        for word, count in data_dict.items():
            if word in posting_list:
                posting_list[word].append((file_index, count))
            else:
                posting_list[word] = [(file_index, count)]

    # Rewrite the posting list
    with open("posting_list.json", "w") as file:
        json.dump(posting_list, file)

os.remove("posting_list.json")

# Generate the output file
with open("output.txt", "w") as file:
    for size, (key, value) in zip(range(len(posting_list)), posting_list.items()):
        vocab[key] = size
        data = ", ".join(map(lambda doc: f"{doc[0]}={doc[1]}", value))
        data = f"{key} ({len(value)}) ==> " + "{" + data + "}\n"
        file.writelines(data)

def query(word):
    """Query a particular word from posting list."""
    if word in posting_list:
        with open("output.txt", "r") as file:
            print(file.readlines()[vocab[word]])
    else:
        print("Word not found in corpora.")
