from Event_Methods import *
import pickle
import os

db = url_database_get_and_load_Events()
auxdb = []
each_cartel = []

for i in range(len(db)):

    cartel = db[i].cartel
    each_cartel = [each_cartel]

    for j in range(len(db[i].cartel)):
        print(each_cartel)
        each_cartel.append(cartel[j].replace(" ",""))
    sorted(each_cartel)
    auxdb.append(each_cartel)


auxdb = sorted(auxdb)
print(auxdb)


