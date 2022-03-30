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

        if product_showdb[0].type == 1:
            if yes_no("Desea escoger este producto del inventario?"):
                client_db[client_index].food.append(product_showdb[0])
                product_showdb[0].amount -= 1
                print("Agregado con exito")
            
        else:
            drink_op = verify_str_indb(["Small", "Medium", "Large"],''' Escriba el tamano de la bebida que desea seleccionar:
            (Este consiente de la capitalizacion de las categorias)
            Small
            Medium
            Large
            ''')

            for i in range(len(product_showdb)):

                if drink_op == product_showdb[i].size:
                    client_db[client_index].food.append(product_showdb[i])
                    product_showdb[i].amount -= 1
                    print("Agregado Con Exito")

                    for j in range(len(food_db)):
                        if product_showdb[i] == food_db[j]:
                            food_db[j] = product_showdb[i]
                            break
                    break
        
        if yes_no("Desea agregar otro producto?"):

            return product_search_client(food_db, client_db, client_index)
            
        else:

            return



def make_bill_food(client_db, client_index = -1):
    '''Makes bill from client obj'''
    total = 0
    subtotal = 0
    totaldescuento = "NO APLICA"
    customer = client_db[client_index]
    print(f''' FACTURA
    
    NOMBRE: {customer.name}
    CEDULA: {customer.dni}
    EDAD: {customer.age}
    ARTICULOS DE COMIDA:
    ''')

    for i in range(len(customer.food)):

        print(f'''
        {customer.food[i].name}
        COSTO SIN IVA: {customer.food[i].price}
        COSTO CON IVA: {customer.food[i].price + customer.food[i].price * 0.16}
        ''')
        subtotal = subtotal + customer.food[i].price + customer.food[i].price * 0.16

    total = subtotal

    print(f'''TOTAL A PAGAR: {total}''')

    if customer.discountfood:
        totaldescuento = total * 0.15
        print (f'''DESCUENTO DEL TOTAL DE: {totaldescuento}''')
        total = total - totaldescuento
        
    
    if yes_no("Desea realizar el pago?"):
        print(f''' *** PAGO REALIZADO EXITOSAMENTE ***
        SUBTOTAL: {subtotal}
        DESCUENTO: {totaldescuento}
        TOTAL: {total}
        ''')
        customer.payedfood = total
        
    return