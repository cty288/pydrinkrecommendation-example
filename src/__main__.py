
import pydrinkrecommendation
import os
from os.path import dirname, join
import sys
from pydrinkrecommendation.drinks import Mood, Taste, Price, Drink

def store_drink():
  print("Please input the following information about the added/updated drink:")
  input_name = input("Name: ")
  input_mood = input("What is the mood of the drink? (1. Happy, 2. Tired): ")
  if(input_mood == "1"):
    input_mood = Mood.Happy
  elif (input_mood == "2"):
    input_mood = Mood.Tired
  else:
    print("Invalid input!")
    return
  
  input_taste = input("Is the drink sweet or bitter? (1. Sweet, 2. Bitter): ")
  if(input_taste == "1"):
    input_taste = Taste.Sweet
  elif (input_taste == "2"):
    input_taste = Taste.Bitter
  else:
    print("Invalid input!")
    return
  
  price_input = input("What is the price of the drink? (1. Cheap, 2. Medium, 3.High): ")
  if(price_input == "1"):
    price_input = Price.Low
  elif (price_input == "2"):
    price_input = Price.Medium
  elif (price_input == "3"):
    price_input = Price.High
  else:
    print("Invalid input!")
    return
  
  pydrinkrecommendation.write_drink(Drink(input_name, input_mood, input_taste, price_input))
  print("Drink successfully added/updated! Check the JSON file to see the changes.")
  
  

def delete_drink():
  input_name = input("What is the name of the drink you want to delete:  ")
  delete_drink = pydrinkrecommendation.delete_drink(input_name)
  if(delete_drink == None):
    print("Drink not found!")
  else:
    print("Drink successfully deleted! Check the JSON file to see the changes.")
  
  
def get_recommendation():
  print("Please input the following information: ")
  
  input_mood = input("Are you happy or tired? (1. Happy, 2. Tired): ")
  if(input_mood == "1"):
    input_mood = Mood.Happy
  elif (input_mood == "2"):
    input_mood = Mood.Tired
  else:
    print("Invalid input!")
    return
  
  input_taste = input("Do you want a sweet or bitter drink? (1. Sweet, 2. Bitter): ")
  if(input_taste == "1"):
    input_taste = Taste.Sweet
  elif (input_taste == "2"):
    input_taste = Taste.Bitter
  else:
    print("Invalid input!")
    return
  
  price_input = input("What is your price range? (1. Cheap, 2. Medium, 3.High): ")
  if(price_input == "1"):
    price_input = Price.Low
  elif (price_input == "2"):
    price_input = Price.Medium
  elif (price_input == "3"):
    price_input = Price.High
  else:
    print("Invalid input!")
    return
  
  drink = pydrinkrecommendation.get_recommendation(input_mood, input_taste, price_input)
  if(drink == None):
    print("The Json file is empty. Please add a drink first.")
  else:
    print("The recommended drink is: " + drink.name + " with a price of " +  Price(drink.price).name + " and a mood of " + Mood(drink.mood).name
          + " and a taste of " + Taste(drink.taste).name)

def main():
  p1 = join(dirname(__file__), 'test.json')
  pydrinkrecommendation.setDefaultPath(p1)
  print("Welcome to the Drink Recommendation System! Drink files are stored in " + p1)
  
  while(True):
    print("What would you like to do?")
    print("1. Store/Update a drink")
    print("2. Delete a drink")
    print("3. Get a drink recommendation")
    print("4. Exit")
    
    val = input("Enter a number: ")
    if(val == "1"):
      store_drink()
    elif(val == "2"):
      delete_drink()
    elif (val == "3"):
      get_recommendation()
    elif (val == "4"):
      break
    else:
      print("Invalid input. Please try again.")
    
  print("Thank you for using the Drink Recommendation System!")
  
  
  
  
  
if __name__ == '__main__':
    main()