
import pydrinkrecommendation
import os
from os.path import dirname, join
import sys
from pydrinkrecommendation.drinks import Mood, Taste, Price, Drink
def main():
  p1 = join(dirname(__file__), 't.json')  
  pydrinkrecommendation.setDefaultPath(p1)
  print(pydrinkrecommendation.get_recommendation(None,None,None).name)
  
if __name__ == '__main__':
    main()