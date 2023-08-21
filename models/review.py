#!/usr/bin/python3
'''
    the implementation of the Review class
'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''
        the implementation for the Review.
    '''
    place_id = ""
    user_id = ""
    text = ""
