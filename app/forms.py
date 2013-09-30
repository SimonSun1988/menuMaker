# -*- coding: utf-8 -*-
from flask.ext.wtf import Form, TextField, SelectField, IntegerField, validators 
from flask.ext.wtf import Required

class addDishForm(Form):
    #~ dish = SelectField(u'dish',choices=[(u'飯類', u'飯類'), (u'麵類', u'麵類')])  
    dish = TextField(u'dish',[validators.Length(min=1, max=30)]) 
    name = TextField(u'name',[validators.Length(min=1, max=30)])
    price = IntegerField(u'price',[validators.NumberRange(min=0, max=99999999)])
               
class addMenuForm(Form):
    giveMenuname = TextField(u'giveMenuname',[validators.Length(min=1, max=30)])
    dish = TextField(u'dish')
    name = TextField(u'name')
    price = TextField(u'price')

