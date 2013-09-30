# -*- coding: utf-8 -*-
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
from pymongo import MongoClient
import datetime

connection = MongoClient()
menu = connection.menu
menu_style = menu.menu_style 
Dumplings = {
    "kind":"foo",
    "name":"bar"
}

menu.menu_style.insert(Dumplings)

for lists in menu_style.find():
    kind = lists['kind']
    name = lists['name']
    price = lists['price']

    print kind, name, price
