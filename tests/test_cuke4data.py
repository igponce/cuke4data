#!/usr/bin/env python
from __future__ import print_function

# import unittest

from cuke4data import gherkin as gkparser

def test_canLoadLibrary():
  return True
    
def test_parseGherkinFromFile():
  source = open("tests/simple.gherkin", 'r')
  gk = gkparser.gherkin()
  gk.parse(source) 
  print("--")
  assert(1 == 2)

def test_parseGherkinFromFile123():
  return True
