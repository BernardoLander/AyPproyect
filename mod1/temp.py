from Event_Methods import *
import pickle
import os

db = url_database_get_and_load_Events()

print(db[0].layout)

