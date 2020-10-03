#!/usr/bin/env python
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import pytest
from cuke4data import gherkin as gkparser

@pytest.fixture
def fixture_unnamedGherkinScenario(fixture):
    scenario_to_test = """
        Given I have a rule like this\n"
        And something happens\n"
        Then do action
    """
    gk = gkparser.gherkin()
    gk.parse(scenario_to_test)
    return gk

class Gherkin_Class_Tests(unittest.TestCase):
    """
    Testcases por individual components (classes).
    """

    def test_createGherkinScenario(self):
        scenarioName = 'Scenario name - string 123'
        sc = gkparser.gherkinScenario(scenarioName)
        assert sc.name == scenarioName

    def test_createGherkinRule(self):
        ruleText = "Given I have a rule text like this one"
        rr = gkparser.gherkinRule(ruleText)
        assert rr.text == ruleText


class Gherkin_Interface_Tests(unittest.TestCase):

    def test_parseGherkinFromFile(self):
        source = open("tests/simple.gherkin", 'r')
        gk = gkparser.gherkin()
        gk.parse(source)
        print("--")
        assert gk.scenarios[0].name == '"Prose to normalize user records"'

    def test_parse_ScenarioName_with_GherkinFromString(self):
        source = """
            Scenario: Test scenario for gherkin

            When I read this content from a string
            And I am not reading from a file
            Then I should be able to parse the file
            """
    
        gk = gkparser.gherkin()
        gk.parse(source)
        # Todo: Dump scenarios
        assert gk.scenarios[0].name == "Test scenario for gherkin"
        assert gk.scenarios[0].rules == []

    def test_unnamed_scenario(self):
        ruleTest = "Given I have a rule like this\n" "And something happens\n" "Then do action\n"

        gk= gkparser.gherkin()
        gk.parse(ruleTest)
        assert gk.scenarios[0].name == "No name"
        assert len(gk.scenarios[0].rules) == 3

    def test_number_of_rules(self):
        ruleTest = "Given I have a rule like this\n" "And something happens\n" "Then do action\n"
        gk= gkparser.gherkin()
        gk.parse(ruleTest)
        assert len(gk.scenarios[0].rules)== 3

# unittest boilerplate 
if __name__ == "__main__":
    unittest.main()