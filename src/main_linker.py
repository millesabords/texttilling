from lemmatizer import *
from similarite import *
from borders import *
from linker import *

input_files = ['../test']

tokenizer = Tokenizer(input_files, 3)#bible.txt'], 3)
(tokens, paragraphs) = tokenizer.preprocess()

print "lemmatizer finished"
print

sim = similarity(tokens)
sim.tfidf()

print 
print "similarity calculs finished"

#B = borders(tokens, sim)
#B.test()

L = linker(input_files, paragraphs, tokens, sim, 0.9)#0.75)
L.process()
