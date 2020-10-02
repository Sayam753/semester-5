import re
import numpy as np


vocab_dict = dict()


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
        f = file.readlines()
        f = f[0].strip().lower()
        f = re.sub(r'[^a-zA-Z\s]', '', f)
        print(f)
    break
#         new_dict = dict(zip(*np.unique(z, return_counts=True)))


with open(f"th-dataset/{file_index}.txt") as file:
    print([f for f in file])


s = "This must notdfew 2412 xb141e deleted, but the number at the end yes 134411"
s = re.sub("\d+", "", s)
print(s,type(s))


help(re.sub)


len(f[0].lower())


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



