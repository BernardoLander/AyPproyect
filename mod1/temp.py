from Event_Classes import Event, Musical, Theater
from Event_Methods import *
from mod1.Event_Methods import url_database_get_and_load_Events
from utilsm1 import get_list_cute
import json
import requests

def main():

    db = url_database_get_and_load_Events()
    event_visualizer(db)


main()