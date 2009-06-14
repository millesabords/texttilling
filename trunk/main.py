from lemmatizer import *
from similarite import *
from borders import *

tokenizer = Tokenizer(['bible.txt'], 3)
tokens = tokenizer.preprocess()

print "lemmatizer finished"
print

sim = similarity(tokens)
sim.tfidf()

print 
print "similarity calculs finished"

B = borders(tokens, sim)
B.test()
