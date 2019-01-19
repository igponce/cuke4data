#!/usr/bin/env python
from __future__ import print_function
import unittest

class GherkinParseFiletests (unittest.TestCase):
  def test_canLoadLibrary(self):
    from gk4data import gherkin
    return True
    
  def test_parseGherkinFromFile(self):
    from gk4data import gherkin
    source = open("simple.gherkin", 'ro')
    gk = gherkin()
    gk.parse(source) 

   
  def test_parseGherkinFromFile123(self):
      return True

if __name__ == "__main__":
    unittest.main()
