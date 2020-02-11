#!/usr/bin/env python
from __future__ import print_function
from cuke4data import gherkin as gkparser


scenario1 = """
    Scenario: Test scenario for gherkin
    When I read this content from a string
    And I am not reading from a file
    Then I should be able to parse the file
"""

scenario2 = """
    Scenario: This scenario has keywords inside.
    When I go to the market
    And it is raining
    And I hear "when you grow-up you'll be able to do that"
    Then I should have 4 gherkin rules, not 5
"""

def test_canLoadLibrary():
    return True

def test_createGherkinRule():
    ruleText = "Given I have a rule text like this one"
    rr = gkparser.gherkinRule(ruleText)
    assert rr.text == ruleText

def test_parseGherkinFromFile():
    source = open("tests/simple.gherkin", 'r')
    gk = gkparser.gherkin()
    out = gk.parse(source.readlines())
    assert(out.scenario_name != None)
    assert(len(out.ruleset) > 0)
    assert(False)

def test_parseGherkinFromString():
    gk = gkparser.gherkin()
    out = gk.parse(scenario1)
    assert(out.scenario_name != None)
    assert(len(out.ruleset) > 0)
    assert(1 > 4)
    return True


def test_createGherkinScenario():
    scenarioName = 'Scenario name - string 123'
    sc = gkparser.gherkinScenario(scenarioName)
    assert sc.scenario_name == scenarioName

