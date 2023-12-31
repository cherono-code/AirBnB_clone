#!/usr/bin/python3
'''
    Containing tests for the state module.
'''
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    '''
        Testing the State class.
    '''

    def test_State_inheritence(self):
        '''
            Testing that State class inherits from BaseModel.
        '''
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        '''
            Testing that State class contains the attribute `name`.
        '''
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    def test_State_attributes_type(self):
        '''
            Testing that State class attribute name is class type str.
        '''
        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)
