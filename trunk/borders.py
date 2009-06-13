from similarite import *
from pylab import *

class borders:
    def __init__(self, tokens, sim):
        self.sim = sim
        self.tokens = tokens

    def test(self):
        for i in xrange(len(self.tokens)):
            # Un document
            X = []
            Y = []
            if len(self.tokens[i]) < 2:
                print "ERROR: de blocs insuffisants"
                return None
            for j in xrange(len(self.tokens[i])):
                # Un bloc
                if j + 1 == len(self.tokens[i]):
                    break
                Y.append(self.sim.cos(i, self.tokens[i][j], self.tokens[i][j + 1]))
                X.append(j)
            plot(X, Y)
            print "showing"
            show()
