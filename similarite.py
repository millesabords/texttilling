import numpy as N

# SIMIlARITE Class
# methode tdidf(self) : elle retourne une liste de tableaux numpy qui contiennent
#                       les coeficients tdidf de chaque terme pour un bloc
# methode cos(self, i, bloc1, bloc2) : retourne le coef de similarite entre deux blocs
#                                      i = le i-eme document
#                                      bloc1 = le premier bloc
#                                      bloc2 = le deuxieme bloc
class similarity:
    # lbt correspond a la liste de listes de listes de termes
    def __init__(self, lbt):
        self.lbt = lbt

    def tfidf(self):
        self.poids = []
        for doc in self.lbt:
            poids = []
            idf = []
            nbBlocs = float(len(doc))
            print "nb blocs = " + str(nbBlocs)

            # Lists containing the number of appearance of a term, which has already been evaluated
            AAstr = []
            AAnb = []
            
            # Construction d'une liste contenant tous les coefficents idf
            for bloc in doc:
                b = N.zeros((len(bloc)))
                for i in xrange(len(bloc)):
                    appear = 0
                    if bloc[i] in AAstr:
                        appear = AAnb[AAstr.index(bloc[i])]
                    else:
                        for j in doc:
                            if bloc[i] in j:
                                appear += 1
                        AAstr.append(bloc[i])
                        AAnb.append(appear)
                    b[i] = N.log(nbBlocs / appear)
                idf.append(b.copy())

            # Calcul des poids tf-idf
            for j in xrange(len(doc)):
                b = N.zeros((len(doc[j])))
                for i in xrange(len(doc[j])):
                    b[i] = float(doc[j].count(doc[j][i])) / len(doc[j])
                b *= idf[j]
                poids.append(b.copy())
                print j
            self.poids.append(poids)

    def cos(self, j, bloc1, bloc2):
        i1 = self.lbt[j].index(bloc1)
        i2 = self.lbt[j].index(bloc2)

        if len(bloc1) < len(bloc2):
            max = len(bloc2)
        else:
            max = len(bloc1)

        b1 = N.zeros((max))
        for i in xrange(len(self.poids[j][i1])):
            b1[i] = self.poids[j][i1][i]
        b2 = N.zeros((max))
        for i in xrange(len(self.poids[j][i2])):
            b2[i] = self.poids[j][i2][i]

        num = N.dot(b1, b2)
        den = N.sqrt(N.dot(b1, b1) * N.dot(b2, b2))
        return (num / den)

