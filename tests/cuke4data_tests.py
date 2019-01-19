#!/usr/bin/env python
from __future__ import print_function

# import unittest

from nose.tools import *
import cuke4data

class GherkinParseFiletestse:
  def test_canLoadLibrary(self):
    return True
    
  def test_parseGherkinFromFile(self):
    source = open("simple.gherkin", 'ro')
    gk = gherkin()
    gk.parse(source) 

  def test_parseGherkinFromFile123(self):
      return True
