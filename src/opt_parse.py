from optparse import OptionParser

class OptParse:
    def __init__(self):
        parser = OptionParser("usage: main.py file1 file2 ...")
        parser.add_option("-d", "--directory", dest="dirname", metavar="DIR", help="Specifier le repertoire de sortie", default="./")
        parser.add_option("-k", "--nb-phrases-bloc", dest="k", metavar="K", help="Specifier le nombre de phrases par bloc. Si non specifie, ce nombre sera evalue via une heuristique", default=3)
        parser.add_option("-f", "--file", dest="files",
                          action="callback", callback=self.vararg_callback, help="Analyse du fichier FILE")
        (options, args) = parser.parse_args()
        self.options = options
        self.args = args

    def vararg_callback(self, option, opt_str, value, parser):
        assert value is None
        value = []

        def floatable(str):
            try:
                float(str)
                return True
            except ValueError:
                return False

        for arg in parser.rargs:
            # stop on --foo like options
            if arg[:2] == "--" and len(arg) > 2:
                break
            # stop on -a, but not on -3 or -3.0
            if arg[:1] == "-" and len(arg) > 1 and not floatable(arg):
                break
            value.append(arg)

        del parser.rargs[:len(value)]
        setattr(parser.values, option.dest, value)
OptParse()
