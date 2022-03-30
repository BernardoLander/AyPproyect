

def topclients_find(db, topclients = []):
   client_db = db
   
   for i in range(len(client_db)):
      cont = 0
      for j in range(len(client_db)):
         if client_db[i] > client_db[j]:
               cont += 1
         elif client_db[i] < client_db[j]:
               cont -= 1
         if cont + 1 == len(client_db):
            topclients.append(client_db[i])
            client_db.pop(i)
            if len(topclients) == 5:
               return topclients
            else:
               return topclients_find(client_db, topclients)

   print (topclients)



def main():


   client_db = [1,2,3,4,5,6,7,8,9]
   print (client_db)
   print(topclients_find(client_db, []))
            

main()