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

import re
import io
# This ruleset has all the magic:
# it stores both the ruleset and de compiled code
# that does all the Gherkin magic.

class gherkinRule:

    def __init__(self, text=None, conjunction=None):
        self.ruleType = None  # (when, given, and) - should have for each - for every
        self.connector = conjunction  # and, or, and not, except (...)
        self.action = None
        self.text = text
    def __repr__(self):
        return f'{__class__}: {self.text}'

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


class gherkinScenario:

    def __init__(self, name='No name'):
        self.name = name.strip()
        self.rules = []
        self.code = None
        self.is_runnable = False

    def __repr__(self):
       return f'{__class__}: {self.name}'

    def add_rule(self, rule: gherkinRule):
        self.rules.append(rule)

class gherkin:

    scenario_keywords = ['scenario',
                         'purpose',
                         'golden', 'golden record',
                         'transform', 'transformation']

    rule_keywords = ['when', 'given', 'since', 'and',
                     'not', 'but', 'except',
                     r'for\s*each', r'for\s*every', 'every',
                     'and', 'or', 'not', 'but']

    rule_actions = ['then', 'log', 'update', 'trigger', 'discard', 'remove']

    def __init__(self):
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

        keywords_regexp = r"^\s*(" + "|".join(self.rule_keywords + self.rule_actions) + ")"
        scenario_regexp = r"^\s*(" + "|".join(self.scenario_keywords) + ")"
        print(keywords_regexp)
        print (scenario_regexp)

        curr_scenario = gherkinScenario()

        # Adapt input

        if source.__class__ is str:
            source = source.splitlines()
       
        for lin in source:
            # Clear whitespace and comments
            lin = lin.lstrip()
            if lin.startswith('#'):
                lin = ''

            if lin != '':
                sp = lin.split(':')
                # Check scenarios first, then rules
                sp = lin.split(':')
                print(lin)

                if len(sp) > 1:
                    print(curr_scenario.name)
                    # Should be a 'Scenario: name' statement
                    if re.match(scenario_regexp, sp[0], re.IGNORECASE) is not None:
                        print("Scenario DETECTED: keyword={}\n\tScenario_name: {}".format(sp[0], sp[1]))
                        new_scenario = gherkinScenario(sp[1])

                        # Do we have already an scenario _with_ rules?
                        if curr_scenario.rules:
                            self.scenarios.append(curr_scenario)
                        else:
                            """ Empty scenario detected 
                                Scenario: blah blah blah <-- this one
                                Scenario: more blah blah blah

                                Should send a warning and ignore the first
                            """
                            print("EMPTY Scenario detected")

                        curr_scenario = new_scenario

                    else:
                        print("UNKNOWN Scenario type detected: {} - Ignoring?".format(sp[0]))
                else:
                    # Whitespace or rule
                    ruleline = re.split(keywords_regexp, lin, 0, re.IGNORECASE)
                    if len(ruleline) > 1:
                        print(f'RULE =>{ruleline}<==')  # gherkin.parse: - Detected Rule {}".format(sp) )
                        conjunction, phrase = ruleline[1], ruleline[2]
                        this_rule = gherkinRule(text=phrase, conjunction=conjunction)
                        curr_scenario.add_rule(this_rule)

                    else:
                        errmsg = 'Expected scenario, rule, comment, or empty line'
                        displaymsg = f'{lin}\n^^^{errmsg}'
                        print(displaymsg)
                        raise RuntimeWarning(errmsg)

        self.scenarios.append(curr_scenario)

