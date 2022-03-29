import requests
import json
from FoodFair_Classes import *
from mod1.utilsm1 import *
from utilsm3 import *


def url_database_get_and_load_FoodFair():
   '''Getting json from url and storing in db'''

   url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json'
   response = requests.request('GET', url)
   json_db = response.json()

   bd = json_db["food_fair_inventory"]

   newdb = []

   for i in range(len(bd)):

      if bd[i]["type"] == 1:

         new_food = food(bd[i]["name"], bd[i]["price"], bd[i]["amount"], bd[i]["type"], bd[i]["presentation"])
         newdb.append(new_food)
      else:

         for j in range(len(bd[i]["price"])):
            
            if j == 0:
               new_food = drink(bd[i]["name"], bd[i]["price"][j], bd[i]["amount"], bd[i]["type"], " Small" )
               newdb.append(new_food)
           
            elif j == 1:
               new_food = drink(bd[i]["name"], bd[i]["price"][j], bd[i]["amount"], bd[i]["type"], " Medium")
               newdb.append(new_food)
            else:
               new_food = drink(bd[i]["name"], bd[i]["price"][j], bd[i]["amount"], bd[i]["type"], " Large")
               newdb.append(new_food)        

   return newdb


def food_fair_vizualizer(db):

   for i in range(len(db)):
      if db[i].type == 1:
         #Comida
         print(f'''Producto Num {i}:
         {db[i].name}
         Precio: {db[i].price}
         Cantidad en Inventario: {db[i].amount}
         Presentacion: {db[i].presentation}''')

      else:
         #bebida
         print(f'''Produto Num {i}:
         {db[i].name + db[i].size}
         Precio: {db[i].price}
         Cantidad en Inventario: {db[i].amount}
         ''')
   
   return

def product_search_manager(db):
   '''Search for products in db by attribute'''

   product_showdb = []
   op = num_verify_range(1,3,'''Indique a travez de que criterio desea ver los productos:
                           1. Buscar por Nombre
                           2. Buscar por Tipo
                           3. Buscar por un rango de precio
                           ''')
   
   if op == 1:
      #By name
      productop = verify_str("Indique el nombre del Producto(En caso de ser una bebida no indique el tamano)")
      

      for i in range(len(db)):

         if db[i].name == productop:
            
            product_showdb.append(db[i])
            food_fair_vizualizer(product_showdb)

            if db[i].type == 1:
                  if yes_no("Desea Eliminar este producto del inventario?"):
                     db.pop(i)
                     print("Eliminado con exito")
                     return
            else:
               drink_op = verify_str_indb(["Small", "Medium", "Large"],''' Indique el tamano de la bebida que desea seleccionar:
               Small
               Medium
               Large
               ''')

               for i in range(len(product_showdb)):

                  if drink_op == product_showdb[i].size:

                     for j in range(len(db)):

                        if product_showdb[i] == db[j]:
                           if yes_no(f"Desea Eliminar este producto del inventario?{db[j].name + db[j].size}?"):
                              db.pop[j]
                              print("Eliminado Con Exito")
                           return

   elif op == 2:

      productop = num_verify_range(1,2,'''Seleccione un tipo de alimento:
      1. Para comida
      2. Para Bebida
      ''')
      for i in range(len(db)):

            if db[i].type == productop:
            
               product_showdb.append(db[i])
               food_fair_vizualizer(product_showdb)
   else:
      #By price range
      
      for i in range(len(db)):
         cont = 0
         for j in range(len(db)):
            if db[i].price > db[j].price:
               cont += 1
            elif db[i].price < db[j].price:
               cont -= 1
            if cont + 1 == len(db):
               maxprice = db[i].price
            

      productoprangemin = num_verify_range



