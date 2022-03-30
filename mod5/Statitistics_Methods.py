



def client_average_spending(client_db):
    '''Calculates average of spending per client'''

    total_spending = 0

    for i in range(len(client_db)):
        total_spending = client_db[i].payed + client_db[i].payedfood + total_spending

    average = total_spending / len(client_db)

    return average

def client_percentage_nobuyfood(client_db):
    '''Finds Percentage of clients that dont buy food'''

    cont = 0
    for i in range(len(client_db)):
        if client_db[i].payedfood == 0:
            cont += 1

    percentage = cont * 100 / len(client_db)

    return percentage

def loyal_clients(db, topclients = []):
    '''Lists top 3 most loyal clients'''
    client_db = db
    for i in range(len(client_db)):
        cont = 0
        for j in range(len(client_db)):
            if client_db[i].payed + client_db[i].payedfood > client_db[j].payed + client_db[j].payedfood:
               cont += 1
            elif client_db[i].payed + client_db[i].payedfood < client_db[j].payed + client_db[j].payedfood:
               cont -= 1
            if cont + 1 == len(client_db):
                topclients.append(client_db[i])
                client_db.pop(i)
                if len(topclients) == 3:
                    return topclients
                else:
                    return loyal_clients(client_db, topclients)


def top_events(db, topevents = []):
    '''Lists top 3 best selling events'''

    event_db = db
    for i in range(len(event_db)):
        cont = 0
        for j in range(len(event_db)):
            if event_db[i].vipqty + event_db[i].genqty > event_db[j].vipqty + event_db[j].genqty:
               cont -= 1
            elif event_db[i].vipqty + event_db[i].genqty < event_db[j].vipqty + event_db[j].genqty:
               cont += 1

            if cont + 1 == len(event_db):
                topevents.append(event_db[i])
                event_db.pop(i)
                if len(topevents) == 3:
                    return topevents
                else:
                    return top_events(event_db, topevents)

def best_food(db, topfood = []):
    '''Lists top 5 best selling foods'''

    food_db = db
    
    for i in range(len(food_db)):
        cont = 0
        for j in range(len(food_db)):
            if food_db[i].amount > food_db[j].amount:

               cont -= 1

            elif food_db[i].amount < food_db[j].amount:
               cont += 1

            if cont + 1 == len(food_db):
                topfood.append(food_db[i])
                food_db.pop(i)

                if len(topfood) == 3:
                    return topfood

                else:
                    return best_food(food_db, topfood)  
            
