# -*- coding: utf-8 -*-
from flask import *
from app import app
from forms import addDishForm, addMenuForm
from dbs import Menudb

@app.route('/')
@app.route('/menu_lists', methods=['GET', 'POST'])
def menu_lists():
    menudb = Menudb()
    menu_names = menudb.getMenusNames()[0]
    menu_dishes = menudb.getMenusNames()[1]
    return render_template('menu_lists.html', menu_names=menu_names)

@app.route('/add_lists', methods=['POST', 'GET'])
def add_lists():
    form = addMenuForm()
    menudb = Menudb()
    items = menudb.getItems()
    if form.validate_on_submit():
        menuAdd_msg = menudb.addMenu(form.giveMenuname.data, request.form.getlist('dish'), request.form.getlist('name'), request.form.getlist('price'))
        if menuAdd_msg == "MenuAddSucess":
            return redirect('menu_lists')
        else:
            menuAdd_msg = menuAdd_msg
            return render_template('add_lists.html', form=form, items=items, error=form.errors, menuAdd_msg=menuAdd_msg)
    return render_template('add_lists.html', form=form, items=items, error=form.errors)
    
@app.route('/menu_dishes', methods=['POST', 'GET'])
def menu_dishes():
    form = addDishForm()
    menudb = Menudb()
    items = menudb.getItems()
    if form.validate_on_submit():
        dishAdd_msg = menudb.addItem(form.dish.data, form.name.data, form.price.data)
        if dishAdd_msg == "DishAddSucess":
            return redirect('menu_dishes')
        else:
            dishAdd_msg = dishAdd_msg
            return render_template('menu_dishes.html', form=form ,items=items ,error=form.errors, dishAdd_msg=dishAdd_msg)
    return render_template('menu_dishes.html', form=form ,items=items ,error=form.errors)

@app.route('/print_menu', methods=['GET','POST'])
def print_menu():
    menudb = Menudb()
    menuName = request.form['inputMenuName']
    getDishes = menudb.searchMenu(menuName)
    return render_template('print_menu.html', menuName=menuName, dishes=getDishes)
    
@app.route('/delDish', methods=['GET','POST'])
def delDish():
    menudb = Menudb()
    dishName = request.form['delDish']
    menudb.delDish(dishName)
    return redirect('menu_dishes')
    
@app.route('/menuDel', methods=['GET','POST'])
def menuDel():
    menudb = Menudb()
    menuName = request.form['menuDel']
    menudb.menuDel(menuName)
    return redirect('menu_lists')

@app.route('/menuEdit', methods=['GET','POST'])
def menuEdit():
    form = addMenuForm()
    menudb = Menudb()
    menuName = request.form['menuEdit']
    getDishes = menudb.searchMenu(menuName)
    items = menudb.getItems()
    return render_template('add_lists.html',form=form, items=items, getDishes=getDishes, menuName=menuName)
    
@app.route('/dbUpdate', methods=['GET','POST'])
def dbUpdate():
    menudb = Menudb()
    menudb.dbUpdate(request.form['menuname'], request.form.getlist('dish'), request.form.getlist('name'), request.form.getlist('price'))
    return redirect('menu_lists')
    
