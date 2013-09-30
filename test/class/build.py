# -*- coding: utf-8 -*-
from pymongo import MongoClient
import datetime

class Myclass(object):
    def __init__(self):
        self.menu_style = MongoClient().menu.menu_style
        
    def addItem(self, kind, name, price):
        module = {
            "kind":kind,
            "name":name,
            "price":price
        }
        
        self.menu_style.insert(module)

    def getMenu(self):  
        menu = []
        for lists in self.menu_style.find():
            menu.append(lists)
    
        return menu

if __name__ == "__main__":
    t = test.getMenu()
    print t
