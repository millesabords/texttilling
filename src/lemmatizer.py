from nltk import *
from os.path import *

l_discriminates = (',','?','[',']','(',')',';','.',':','/','!','a',
                   'an','of','this','in','but','to','from',
                   'this','a',',','that','and','have','-','who',
                   ' ','are','s','.','has','will','is','it','the',
                   'which','for','be','by','on','with','an','as',
                   'them','they','or','their','than','thi','would',
                   'then','so','hi','if','at','%')

class Tokenizer:
    def __init__(self, files, k):
        self.files = files
        self.k = k
    
    def filter(self, token):
        if token in l_discriminates:
            return False
        else:
            return True
    
    def stemming(self, toks, occurences):
        """
        le "stemming" ou decoupage des mots pour les regrouper sous
        un nombre plus restreints de mots qui fasse apparaitre des "familles".
        """
        stemmer = nltk.PorterStemmer()
        tokens = toks
        stems = []

        for token in tokens:
            stemmed_token = stemmer.stem(str.lower(token))
            if self.filter(stemmed_token) == True:
                stems.append(stemmed_token)
                
                #comptage des occurences
                if occurences.has_key(stemmed_token) == False:
                    occurences[stemmed_token] = 1
                else:
                    occurences[stemmed_token] += 1
#            else:
#                print stemmed_token

        return stems
        
    def tokenizing(self, tex, k):
        """
        La partie sensible du programme. Le decoupage des paragraphes n'est pas encore extra.
        """
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
        """
        Renvoie tout le contenu du (des) fichier(s).
        """
        res = []
    #    for w in nltk.corpus.gutenberg.words('austen-emma.txt'):
    #        res[0] += w + ' '
    
    #    for w in nltk.corpus.gutenberg.words('shakespeare-hamlet.txt'):
    #        res[1] += w + ' '
            
        for file in range(0, len(self.files)):
            res.append('')
            if (os.path.isdir(self.files[file])):
                for root, dirs, files in os.walk(self.files[file]): 
                    for i in files: 
                        input = open(os.path.join(root, i), 'r')
                        lines = input.readlines()[0:]
                        for l in lines:
                            res[file] += l
                        print files
            else:
                input = open(self.files[file], 'r')
                lines = input.readlines()[0:]
                for l in lines:
                    res[file] += l
        return res


    def tab_occurences(self, occurences):
        """
        affichage des occurences du texte en cours.
        """
        print "\nTable des occurences: "
        cpt = 0
        sss = ""
        loc = occurences.items()
        loc.sort()
        for i in loc:
            cpt += 1
            rrr = str(i[0]) + ": " + str(i[1])
            if len(rrr) > 7:
                rrr += '\t'
            else:
                rrr += '\t\t'
            sss += rrr
            if cpt == 6:
                print sss
                cpt = 0
                sss = ""
        print "number of different occurences in this text: " + str(len(occurences))

        
    def preprocess(self):
        """
        lance le tokenizing puis le stemming sur tout le corpus.
        """
        tok = []

        corpus = self.getCorpus()
        paragraphs = []
        for i in range(0, len(self.files)):
            tok.append([])
            bloks = self.tokenizing(corpus[i], self.k)

            occurences = {}
            for b in bloks:
                tok[i].append(self.stemming(b, occurences))
            paragraphs.append(bloks)
            self.tab_occurences(occurences)

        return (tok, paragraphs)
