from __future__ import print_function
import re

# This ruleset has all the magic:
# it stores both the ruleset and de compiled code that does all the Gherkin magic.

class gherkinScenario:

    name = None
    ruleset = None
    code = None

    def __init__ (self, name = 'Sample Scenario'):
        self.name = name
        ruleset = None
        code = None
     

class gherkinRule:
    ruleType =  None # (when, given, and)
    connector = None # and, or, and not, except (...)
    text = None

    def __init__ (self, text=None) :
        self.text = text
        


class gherkin:

    scenario_keywords = ['scenario', 'golden', 'golden record', 
                         'transform', 'transformation' ]

    rule_keywords = ['when','given', 'since', 'and', 'not', 'but', 'except',
                     r'for\s*each', r'for\s*every', 'every', 'and', 'or', 'not', 'but' ]

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

        Scenario|Transfor(mation)|Golden Record: "__name__":

        ^Given|When|^_____ .....
        ^And^Or^Not ____________
        Then ___________________
        """

        keywords_regexp = r"^\s*(" + "|".join(self.rule_keywords) + "|".join(self.rule_actions) + ")"
        scenario_regexp = r"^\s*(" + "|".join(self.scenario_keywords) + ")"
        print( keywords_regexp ); print (scenario_regexp)

        scenario = []
        curr_scenario = []
        
        for lin in source:

            # Clear whitespace and comments

            lin = lin.lstrip()
            if lin.startswith('#') :
               lin = ''

            if lin != '':
                # Check scenarios first, then rules
                sp = lin.split(':') 

                if len(sp) > 1 :
                   # Should be a 'Scenario: name' statement
                   if ( re.match(scenario_regexp, sp[0], re.IGNORECASE ) != None ) :
                       print("Scenario DETECTED: {}\n\tScenario_name: {}".format(sp[0],sp[1]))
                   else :
                       print ("UNKNOWN Scenario type detected: {} - Ignoring?".format(sp[0]))
                else:
                   # Whitespace or rule
                   ruleline = re.split(keywords_regexp, lin, 0, re.IGNORECASE)
                   if len(ruleline) > 1 :
                      print(ruleline); # gherkin.parse: - Detected Rule {}".format(sp) )
                   else:
                      print("gherkin_parse: - notArule {}".format(ruleline)) 

        #if type(source).__name__ in ('file','TextOIWrapper'):
        #    source.close()

