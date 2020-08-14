from pprint import pprint
from gensim import corpora
from collections import defaultdict


text_corpus = [
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    "System and human system engineering testing of EPS",
    "Relation of user perceived response time to error measurement",
    "The generation of random binary unordered trees",
    "The intersection graph of paths in trees",
    "Graph minors IV Widths of trees and well quasi ordering",
    "Graph minors A survey",
]

a = defaultdict(int)

stoplist = set('for a of the and to in'.split(' '))

texts = [[word for word in tokens.lower().split() if word not in stoplist] for tokens in text_corpus]

for i in texts:
    for j in i:
        a[j] += 1

processed_corpus = [[token for token in text if a[token] > 1] for text in texts]

pc = corpora.Dictionary(processed_corpus)
pprint(pc.token2id)