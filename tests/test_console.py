#!/usr/bin/python3
"""Define unittests console.py

    Unittest classes
        TestHBNBCommand_Prompting
        TestHBNBCommand_help
        TestHBNBCommand_exit
        TestHBNBCommand_creat
        TestHBNBCommand_show
        TestHBNBCommand_all
        TestHBNBCommand_destroy
        TestHBNBCommand_update
    """


import os
 import sys
import unittest
from models import storage
from models.engine.file_stroage import FileStorage
from console import H
