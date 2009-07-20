from similarite import *
from pylab import *

class borders:
    def __init__(self, tokens, sim):
        self.sim = sim
        self.tokens = tokens
        self.Xs = []
        self.Ys = []
        self.B = []

    def coordinates(self):
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
            self.Xs.append(X[:])
            self.Ys.append(Y[:])

            plot(X, Y)

    def getD(self, y, i):
        itmp = i
        maxRight = 0.
        maxLeft = 0.
        while itmp > 0 and y[itmp - 1] > y[itmp]:
            maxRight = y[itmp - 1]
            itmp -= 1
        itmp = i
        while itmp < len(y) - 1 and y[itmp + 1] > y[itmp]:
            maxLeft = y[itmp + 1]
            itmp += 1
        if maxRight != 0.:
            maxRight -= y[i]
        if maxLeft != 0.:
            maxLeft -= y[i]
        return maxRight + maxLeft

    def borders(self):
        print
        print "Determining the text's borders"
        for y in self.Ys:
            depths = []
            borders = []
            for i in xrange(len(y)):
                depths.append(self.getD(y, i))
            m = mean(depths)
            s = std(depths)
            for i in xrange(len(depths)):
                if depths[i] > m - s / 2:
                    borders.append(i)
                    plot([i, i], [0., 1.], 'r')
            self.B.append(borders[:])

            show()
