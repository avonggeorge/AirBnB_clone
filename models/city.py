#!/usr/bin/python3
"""
module which contain a class that inherits from
the BaseModel as its parent class
"""
from base_model import BaseModel


class City(BaseModel):
    """
    Subclass which inherits from the BaseModels class
    sharing its properties and methods
    """
    state_id = ""
    name = ""
