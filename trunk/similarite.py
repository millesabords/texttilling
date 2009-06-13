import numpy as N

# SIMIlARITE Class
# methode tdidf : elle retourne une liste de tableaux numpy qui contiennent
#                 les coeficients tdidf de chaque terme pour un bloc
class similarite:
    # lbt correspond a la liste de liste de termes
    def __init__(self, lbt):
        self.lbt = lbt

    def tfidf(self):
        poids = []
        idf = []
        nbBlocs = float(len(self.lbt))
        # Construction d'une liste contenant tous les coefficents idf
        for bloc in self.lbt:
            b = N.zeros((len(bloc)))
            for i in xrange(len(bloc)):
                appear = 0
                for j in self.lbt:
                    if j.count(bloc[i]) != 0:
                        appear += 1
                b[i] = N.log(nbBlocs / appear)
            idf.append(b.copy())
        for j in xrange(len(self.lbt)):
            b = N.zeros((len(self.lbt[j])))
            for i in xrange(len(self.lbt[j])):
                b[i] = float(self.lbt[j].count(self.lbt[j][i])) / len(self.lbt[j])
            b *= idf[j]
            poids.append(b.copy())
        self.poids = poids

    def cos(self, bloc1, bloc2):
        i1 = self.lbt.index(bloc1)
        i2 = self.lbt.index(bloc2)

        if len(bloc1) < len(bloc2):
            max = len(bloc2)
        else:
            max = len(bloc1)

        b1 = N.zeros((max))
        for i in xrange(len(self.poids[i1])):
            b1[i] = self.poids[i1][i]
        b2 = N.zeros((max))
        for i in xrange(len(self.poids[i2])):
            b2[i] = self.poids[i2][i]

        num = N.dot(b1, b2)
        den = N.sqrt(N.dot(b1, b1) * N.dot(b2, b2))
        return (num / den)

