from mod1.utilsm1 import *
from FoodFair_Methods import *




def main():
    db = url_database_get_and_load_FoodFair()


    for i in range(len(db)):
        cont = 0
        for j in range(len(db)):
            if db[i].price > db[j].price:
               cont += 1
            elif db[i].price < db[j].price:
               cont -= 1
            if cont + 1 == len(db):
               maxprice = db[i].price
    
    print(maxprice)

main()