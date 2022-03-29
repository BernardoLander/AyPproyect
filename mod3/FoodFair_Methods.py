import requests
import json
from FoodFair_Classes import *


def url_database_get_and_load_FoodFair():
   '''Getting json from url and storing in db'''

   url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json'
   response = requests.request('GET', url)
   json_db = response.json()

   bd = json_db["food_fair_inventory"]

   newdb = []

   for i in range(len(bd)):

      if len(bd[i]["price"]) == 1:

         new_food = food(bd[i]["name"], bd[i]["price"], bd[i]["amount"], bd[i]["presentation"], bd[i]["type"])
         newdb.append(new_food)
      else:

         for j in range(len(bd[i]["price"])):
            
            new_food = food(bd[i]["name"], bd[i]["price"][j], bd[i]["amount"], bd[i]["presentation"], bd[i]["type"])
            newdb.append(new_food)           

   return newdb