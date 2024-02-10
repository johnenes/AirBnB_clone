#!/usr/bin/python3

"""Defines the BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
        """BaseModel for the AirBnB project"""
        def __init__(self, *args, **kwargs):
                """Initalize a new BaseModel
                
                Args:
                    *args (any) Unused
                    **kwargs (dict)" key/value pairs  of attribute

                """
                tform = "%Y-%m-%dT%H:%M:%S.%f"
                self.id = str(uuid4())
                self.create_at = datetime.today()
                self.update_at = datetime.today()
                if len(kwargs) != 0:
                        for key, value in kwargs.items():
                               if key == "create_at" or key == "update_at":
                                       self.__dict__[key] = datetime.strftime(value,tform)

                               else:
                                       self.__dict__[key] = value
                else:
                        models.storage.new(self)

                def save(self):
                        """Update update_at with the current datetime"""
                        self.update_at = datetime.today()
                        models.storage.save()
                
                def to_dict(self):
                        """Return the dictionary of the Basemodel instance
                        
                        include the kay and value pair __class__ representing
                        the class name of the object
                        """

                        rdict = self.__dict__.copy()
                        rdict["create_at"]= self.create_at.isoformat()
                        rdict["update_at"] = self.update_at.isoformat()
                        rdict["__class__"] = self.__class__.__name__
                        return rdict
                

                def __str__(self):
                        """Return the print/str representation of the BaseModel instance"""
                        clsName = self.__class__.__name__
                        return "[{}]({}){}".format(clsName,self.id, self.__dict__)

