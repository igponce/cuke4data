# -*- coding: utf-8 -*-
#    Copyright 2020 Iñigo Gonzalez Ponce
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from __future__ import print_function
import re

# This ruleset has all the magic:
# it stores both the ruleset and de compiled code
# that does all the Gherkin magic.


class gherkinScenario:

    def __init__(self, name='Sample Scenario'):
        self.name = name.strip()
        self.rules = []
        self.code = None

    def __str__(self):
       return self.name


class gherkinRule:

    def __init__(self, text=None, conjunction=None):
        self.ruleType = None  # (when, given, and) - should have for each - for every
        self.connector = conjunction  # and, or, and not, except (...)
        self.action = None
        self.text = text

    def match(self,text):
        """
        Check if this text matches a rule to  be excecuted
        """
        return False

    def exec(self,code):
        """
        Execute piece of code if rule matches.
        """
        return False


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
            self.scenarios = []

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


        keywords_regexp = r"(?!=^\s*)   (" + "|".join(self.rule_keywords) + \
                          "|".join(self.rule_actions) + ")"
        scenario_regexp = r"^\s*(" + "|".join(self.scenario_keywords) + ")"
        print(keywords_regexp)
        print (scenario_regexp)

        scenario = []
        curr_scenario = []

        # Adapt input

        if source.__class__ is str:
            source = source.splitlines()
       
        for lin in source:
            # Clear whitespace and comments
            lin = lin.lstrip()
            if lin.startswith('#'):
                lin = ''

            if lin != '':
                # Check scenarios first, then rules
                sp = lin.split(':')
                print(lin)

                if len(sp) > 1:
                    # Should be a 'Scenario: name' statement
                    if re.match(scenario_regexp, sp[0], re.IGNORECASE) is not None:
                        print("Scenario DETECTED: keyword={}\n\tScenario_name: {}".format(sp[0], sp[1]))
                        scenario = gherkinScenario(sp[1])
                    else:
                        print("UNKNOWN Scenario type detected: {} - Ignoring?".format(sp[0]))
                else:
                    # Whitespace or rule
                    ruleline = re.split(keywords_regexp, lin, 0, re.IGNORECASE)
                    if len(ruleline) > 1:
                        print(f'RULE =>{ruleline}<==')  # gherkin.parse: - Detected Rule {}".format(sp) )
                        _, conjunction, phrase = ruleline
                        this_rule = gherkinRule(text=phrase, conjunction=conjunction)
                        self.scenarios[-1].rules.append(this_rule)

                    else:
                        print("gherkin_parse: - notArule {}".format(ruleline))

        if scenario != []:
            # Scenario detected
            if self.scenarios == None:
               self.scenarios = [scenario]
            else:
               self.scenarios += [scenario]
            # No scenario detected. Create dummy one
        else:
            self.scenarios = [ gherkinScenario('No name')]

        # if type(source).__name__ in ('file','TextOIWrapper'):
        #     source.close()
