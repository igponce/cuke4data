from __future__ import print_function
import re
import io
# This ruleset has all the magic:
# it stores both the ruleset and de compiled code
# that does all the Gherkin magic.


class gherkinScenario:

    scenario_name = None
    ruleset = None
    code = None

    def __init__(self, name='Sample Scenario'):
        self.scenario_name = name
        ruleset = []
        code = []


class gherkinRule:
    ruleType = None  # (when, given, and)
    connector = None  # and, or, and not, except (...)
    text = None

    def __init__(self, text=None, ruleType=None, connector=None):
        self.text = text
        self.ruleType = ruleType
        self.connector = None


class gherkin:

    scenario_keywords = ['scenario', 'golden', 'golden record',
                         'transform', 'transformation']

    rule_keywords = ['when', 'given', 'since', 'and',
                     'not', 'but', 'except',
                     r'for\s*each', r'for\s*every', 'every',
                     'and', 'or', 'not', 'but']

    rule_actions = ['then', 'log', 'update', 'trigger', 'discard', 'remove']

    def __init__(self, debug=True):
        if (debug):
            print("gherkin: __init__ ")

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
    def parse(self, source):
        def iterate_lines(ii):
            print("iterate_lines: type={}".format(type(ii)))

            if type(ii) == str:
                return ii.splitlines()
            elif type(ii) == io.TextIOWrapper:
                return ii.readlines()
            else:
                return ii

        keywords_regexp = r"^\s*(" + "|".join(self.rule_keywords) + \
                          "|".join(self.rule_actions) + ")"
        scenario_regexp = r"^\s*(" + "|".join(self.scenario_keywords) + ")"

        scenario = []
        curr_scenario = []
        
        for lin in iterate_lines(source):
            # Clear whitespace and comments
            lin = lin.lstrip()
            if lin.startswith('#'):
                lin = ''

            if lin != '':
                # Check scenarios first, then rules
                print("Not whitespace line 80: {}".format(lin))
                sp = lin.split(':')

                if len(sp) > 1:
                    # Should be a 'Scenario: name' statement
                    if re.match(scenario_regexp, sp[0], re.IGNORECASE) is not None:
                        scenario = gherkinScenario(sp[1])

                    else:
                        print("UNKNOWN Scenario type detected: {} - Ignoring?".format(sp[0]))
                else:
                    # Whitespace or rule
                    ruleline = re.split(keywords_regexp, lin, 0, re.IGNORECASE)
                    if len(ruleline) > 1:
                        print(ruleline)  # gherkin.parse: - Detected Rule {}".format(sp) )p
                    else:
                        print("gherkin_parse: - notArule {}".format(ruleline))

        return scenario

        # if type(source).__name__ in ('file','TextOIWrapper'):
        #     source.close()
