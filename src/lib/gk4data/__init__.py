# Gherkin4Data
__version__ = "0.0.1"
__package__ = "gk4data"
__doc__ = """
Gherkin4Data

Simple gherkin parser tied to data handling.
By now we have only two methods:

- Parse ()

   This method understands just a subset of the Gherkin language
   tailored for simple data needs.

        Semi-BNF for the Gherkin-data language is:

        Scenario|Thansformation "______":

        ^Given|When|^_____ .....
        ^And^Or^Not ____________
        Then ___________________
        
    *** Gherkin data tables is not supported. This is not for testing ***
    
"""

from .gherkin import gherkin