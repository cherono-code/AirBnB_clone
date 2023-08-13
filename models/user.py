#!/usr/bin/python3
'''
    the implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
        the Definition of the User class
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
