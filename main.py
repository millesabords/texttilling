from lemmatizer import *
from similarite import *
from borders import *

tokenizer = Tokenizer(['heracles.txt'], 3)
tokens = tokenizer.preprocess()

sim = similarity(tokens)
sim.tfidf()

B = borders(tokens, sim)
B.test()
