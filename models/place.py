#!/usr/bin/python3
"""Define the place class"""
from model.base_model import BaseModel

class Place(BaseModel):
    """ Represent a  place  with 
    
    Attributes:
        city_id (str): The city id
        User_id (str) : The User id
        name(str): The name of the place
        description (str): The description of the place
        number_room(int): number of rooms of the place
        number of bathrooms (int): The number of bathrooms of the place
        max_guest (init):The maximum number of guest of the place
        pricce_by_night(init): The price by night of the place
        latitude(float): The latitude of the place
        longitude(float): The longitude of the place 
        amenity_id (list) : A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

