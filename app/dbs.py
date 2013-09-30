# -*- coding: utf-8 -*-
from pymongo import MongoClient
import datetime

class Menudb(object):
    def __init__(self):
        self.menu_style = MongoClient().menu.menu_style
        self.menu_lists = MongoClient().menu.menu_lists
        
    def addItem(self, dish, name, price):
        module = {
            "dish":dish,
            "name":name,
            "price":price
        }
        
        if self.menu_style.find_one({"name":name}):
            return "DishAddError"        
        else:
            self.menu_style.insert(module)
            return "DishAddSucess"

    def getItems(self):  
        menu = []
        for lists in self.menu_style.find():
            menu.append(lists)
        return menu
        
    def addMenu(self, menu_name, dish_list, name_list, price_list):
        menu_lists = {
            "menu_name":menu_name,
            "menu_dishes":[]
        }
        
        if  self.menu_lists.find_one({"menu_name":menu_name}):
            return "MenuAddError"
        else:
            for num in  range(len(price_list)):
                module = {"dish":dish_list[num],"name":name_list[num],"price":price_list[num]}        
                menu_lists['menu_dishes'].append(module)
            self.menu_lists.insert(menu_lists)
            return "MenuAddSucess"
    
    def getMenusNames(self):
        menuNames = []
        menuDishes = []
        for menu in self.menu_lists.find():
            menuNames.append(menu['menu_name'])
            menuDishes.append(menu['menu_dishes'])
        return menuNames, menuDishes
        
    def searchMenu(self, menu_name):
        dishes = []
        getMenu = self.menu_lists.find_one({"menu_name": menu_name})
        for dish in getMenu['menu_dishes']:
            dishes.append(dish)
        return dishes
                
    def delDish(self, dishname):
        self.menu_style.remove({"name":dishname})
    
    def menuDel(self, menu_name):
        self.menu_lists.remove({"menu_name":menu_name})
        
    def dbUpdate(self, menu_name, dish_list, name_list, price_list):
        menu_lists = {
            "menu_name":menu_name,
            "menu_dishes":[]
        }
        
        if self.menu_lists.find_one({"menu_name": menu_name}):
            self.menu_lists.remove({"menu_name":menu_name})
            #~ ori_dishes = self.menu_lists.find_one({"menu_name": menu_name})['menu_dishes']
            #~ print ori_dishes

        for num in range(len(price_list)):
            module = {"dish":dish_list[num],"name":name_list[num],"price":price_list[num]}        
            menu_lists['menu_dishes'].append(module)
        self.menu_lists.insert(menu_lists)
            
            
        
        
        
if __name__ == "__main__":
    test = Menudb()
    test.dbUpdate("嘿嘿黑",['a','b'],['c','d'],[5,10])
