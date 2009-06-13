from nltk import *

class Tokenizer:
    def __init__(self, files, k):
        self.files = files
        self.k = k
    
    def filter(self, token):
        if token == ',' or token == '?' or token == '[' or token == ']' or token == '(' or token == ')' or token == ';' or token == '.' or token == ':' or token == '/' or token == '!' or token == 'a' or token == 'the' or token == 'an':
            return False
        else:
            return True
    
    def stemming(self, toks):
        stemmer = nltk.PorterStemmer()
        tokens = toks
        stems = []
        
        for token in tokens:
            stemmed_token = stemmer.stem(token)
            if self.filter(stemmed_token) == True:
                stems.append(stemmed_token)
            
        return stems
        
    def tokenizing(self, tex, k):
        text = tex
        pattern = r'''(?x)
        \w+
        | \$?\d+(\.\d+)? 
        | ([A-Z]\.)+ 
        | [^\w\s]+ '''
        tokens = nltk.tokenize.regexp_tokenize(text, pattern)
        blok = [[]]
        
        sentences = 0
        for t in tokens:
            
            blok[len(blok) - 1].append(t)
            if t == '.':
                sentences += 1
                if sentences % k == 0:
                    blok.append([])
        
        return blok
        
    def getCorpus(self):
        res = []
    #    for w in nltk.corpus.gutenberg.words('austen-emma.txt'):
    #        res[0] += w + ' '
    
    #    for w in nltk.corpus.gutenberg.words('shakespeare-hamlet.txt'):
    #        res[1] += w + ' '
            
        for file in range(0, len(self.files)):
            res.append('')
            input = open(self.files[file], 'r')
            lines = input.readlines()[0:]
            for l in lines:
                res[file] += l
        
        return res
        
    def preprocess(self):
        tok = []
        
        corpus = self.getCorpus()
        
        for i in range(0, len(corpus)):
            tok.append([])
            
            bloks = self.tokenizing(corpus[i], self.k)
            
            for b in bloks:
                tok[i].append(self.stemming(b))
            
        return tok
