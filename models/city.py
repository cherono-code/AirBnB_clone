#!/usr/bin/python3
'''
    Defining the class City.
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
        Defining the class City that inherits from BaseModel.
    '''
    state_id = ""
    name = ""
