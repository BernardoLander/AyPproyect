from xxlimited import foo
from mod3.FoodFair_Methods import food_fair_vizualizer, get_price_limits
from mod3.utilsm3 import *



def product_search_client(food_db, client_db, client_index):
        '''Search for products in food_db by attribute'''

        food_fair_vizualizer(food_db)
        product_showdb = []

        productop = verify_str("Indique el nombre del Producto(En caso de ser una bebida no indique el tamano)")
        

        for i in range(len(food_db)):

                if food_db[i].name == productop:
                
                    product_showdb.append(food_db[i])
                    food_fair_vizualizer(product_showdb)

                    if food_db[i].type == 1:
                        if yes_no("Desea escoger este producto del inventario?"):
                            client_db[client_index].food.append(food_db[i])
                            print("Agregado con exito")
                            break
                    else:
                        drink_op = verify_str_indb(["Small", "Medium", "Large"],''' Indique el tamano de la bebida que desea seleccionar:
                        Small
                        Medium
                        Large
                        ''')

                        for i in range(len(product_showdb)):

                            if drink_op == product_showdb[i].size:
                                client_db[client_index].food.append(product_showdb[i])
                                print("Agregado Con Exito")
                                break
                    
                    break
        
        if yes_no("Desea agregar otro producto?"):

            return product_search_client(food_db, client_db, client_index)
            
        else:

            return

