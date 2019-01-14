from __future__ import print_function
import re

class gherkin:

    rule_keywords = ['given', 'since', 'and', 'not', 'but', 'except',
                     'for each', 'for every', 'every' ]

    rule_actions = [ 'then', 'log', 'update', 'trigger', 'discard', 'remove' ]

    def __init__(self, debug = True):
        if (debug):
            print("gherkin: __init__ ")
        
    def parse ( source ):

        """
        Parse gherkin from source. Source can be *whatever* we need
        (stream or string/stingarray).

        Since we are using Gherkin for data stuff, scenarios are not needed.
        This makes "a bit" simpler the Gherkin parsing (by now).

        Semi-BNF for the Gherkin-data language is:

        Scenario|Thansformation "______":

        ^Given|When|^_____ .....
        ^And^Or^Not ____________
        Then ___________________
        """

        keywords_regexp = "^\s+(" + rule_keywords.join("|") + ")\s(.)"
        print( keywords_regexp )

        for lin in source:


            sp = re.split()
