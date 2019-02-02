#!/usr/bin/env python
from __future__ import print_function

from cuke4data import gherkin as gkparser

def test_canLoadLibrary():
  return True
    
def test_parseGherkinFromFile():
  source = open("tests/simple.gherkin", 'r')
  gk = gkparser.gherkin()
  gk.parse(source) 
  print("--")
  # assert(1 == 2)

def test_parseGherkinFromString():
  source = """
     Scenario: Test scenario for gherkin

     When I read this content from a string
     And I am not reading from a file
     Then I should be able to parse the file
     """
  
  gk = gkparser.gherkin()
  gk.parse(source)



  return True

def test_createGherkinScenario():

  scenarioName = 'Scenario name - string 123'
  sc = gkparser.gherkinScenario(scenarioName)

  assert sc.name == scenarioName
