from lemmatizer import *
from similarite import *
from borders import *
from linker import *
from opt_parse import OptParse

opts = OptParse()

if len(opts.args) != 0 or opts.options.files == None or len(opts.options.files) == 0:
    print "usage: main.py -f file1 file2 file3 ..."
    exit(1)
input_files = opts.options.files

tokenizer = Tokenizer(input_files, int(opts.options.k))
(tokens, paragraphs) = tokenizer.preprocess()

print "lemmatizer finished"
print

sim = similarity(tokens)
sim.tfidf()

print 
print "similarity calculs finished"

B = borders(tokens, sim)
B.coordinates()
B.borders()

L = linker(opts.options.dirname, input_files, paragraphs, tokens, sim, 0.85)
L.process()
