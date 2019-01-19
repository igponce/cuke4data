from __future__ import print_function
import re

# This ruleset has all the magic:
# it stores both the ruleset and de compiled code that does all the Gherkin magic.

class gherkinRuleset:

    ruleset = None
    code = None


class gherkinRule:
    ruleType =  None # (when, given, and)
    connector = None # and, or, and not, except (...)


class gherkin:

    rule_keywords = ['given', 'since', 'and', 'not', 'but', 'except',
                     'for\s*each', 'for\*every', 'every' ]

    rule_actions = [ 'then', 'log', 'update', 'trigger', 'discard', 'remove' ]

    def __init__(self, debug = True):
        if (debug):
            print("gherkin: __init__ ")
        
    def parse (self, source):

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

        keywords_regexp = "^\s+(" + "|".join(self.rule_keywords) + ")\s(.)"
        print( keywords_regexp )
        
        for lin in source:

            # Clear whitespace and comments

            lin = lin.lstrip()
            if lin.startswith('#') :
               lin = ''

            if lin != '':
               sp = re.split(keywords_regexp, lin)
               print("gherkin.parse: {}".format(sp))


        if type(source).__name__ in ('file','TextOIWrapper'):
            source.close()

