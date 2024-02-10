#!/usr/bin/python3
"""Define the state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state

    Attribute:
    name(str): the name of the state
    """
    name = ""
