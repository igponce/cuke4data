#!/usr/bin/env python
from __future__ import print_function
from cuke4data import gherkin as gkparser


scenario1 = """
    Scenario: Test scenario for gherkin

    When I read this content from a string
    And I am not reading from a file
    Then I should be able to parse the file
"""

def test_canLoadLibrary():
    return True


def test_parseGherkinFromFile():
    source = open("tests/simple.gherkin", 'r')
    gk = gkparser.gherkin()
    gk.parse(source.readlines())
    print("--")


def test_parseGherkinFromString():

    gk = gkparser.gherkin()
    out = gk.parse(scenario1)
    
    print("test_parseGherkinFromString: {}".format(out))
    assert(out.scenario_name != None)
    # Todo: Dump scenarios
    return True


def test_createGherkinScenario():
    scenarioName = 'Scenario name - string 123'
    sc = gkparser.gherkinScenario(scenarioName)
    assert sc.scenario_name == scenarioName


def test_createGherkinRule():
    ruleText = "Given I have a rule text like this one"
    rr = gkparser.gherkinRule(ruleText)
    assert rr.text == ruleText
