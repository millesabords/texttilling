from similarite import *
from pylab import *

class linker:
    """
    le resultat du linkage sera un fichier nomme comme le fichier original,
    auquel on concatene "res".
    """

    def __init__(self, input_files, tokens, sim, seuil):
        self.sim = sim
        self.tokens = tokens
        self.seuil = seuil
        self.input_files = input_files

    def create_links(self):
        """
        creer le tableau des liens en 3 boucles:

        pour chaque fichier,
          pour chaque paragraphe
            pour tous les autres paragraphes
              regarder le coefficient de "ressemblance" calcule par charles grace a la lib nltk (...)
              si ce coeff depasse le seuil (a determiner),
              alors c'est que ce paragraphe est lie a celui en cours
              d'etude, et donc on rajoute ce lien dans le tableau de liens
        """
        lnks = []
        for i in xrange(len(self.tokens)):
            tab1 = []
            for j in xrange(len(self.tokens[i])):
                tab2 = []
                for k in xrange(len(self.tokens[i])):
                    if j != k:
                        coeff = self.sim.cos(i, self.tokens[i][j], self.tokens[i][k])
                        if coeff > self.seuil:
                            #print coeff#debug to adjust seuil
                            tab2.append(k)
                tab1.append(tab2)
            lnks.append(tab1)
        return lnks


    def process(self):
        """
        lance create_links() et recupere le resultat dans le tableau lnks[],
        qui est a trois dimensions (fichiers, paragraphes, mots).
        ensuite il affiche ces resultats, ce qui pose un probleme a l'heure actuelle (voir commentaires)
        """
        print "Link stage started.."
        lnks = self.create_links()

        for i in xrange(len(self.input_files)):
            output = open(self.input_files[i] + "res", 'w')
            #ici jaurai besoin des paragraphes coupes mais non transformes (re-ecrivables)
            #pour creer le beau fichier tel qu'on en parlait dans les specs
            for j in xrange(len(lnks[i])):
                if len(lnks[i][j]) > len(lnks[i]) / 2:
                    s = "paragraph " + str(j) + " is linked with almost everything\n"
                else:
                    s = "paragraph " + str(j) + " is linked with:\t" + str(lnks[i][j]) + '\n'
                if len(lnks[i][j]) == 0:
                    s = "paragraph " + str(j) + " has no links\n"
                output.write(s)
        print "link stage finished"
