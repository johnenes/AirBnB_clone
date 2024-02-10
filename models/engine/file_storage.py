import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import  City
from models.place import Place
from models.review import Review
from models.amenity import Amenity



class FileStorage:
    """Representing an abstraction storage engine
    
    
        Attributes:
            __file_path(str): The name of the file to save objects to.
            __objects(dict): A dictionary of instantiated objects    
    """
    
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Return the dictioanry __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects obj with new key id"""
        object_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_name, obj.id)] = obj
  
  
    def save(self):
        """Serialization  __objects to JSON file __file_json"""
        o_dict = FileStorage.__objects
        objectdict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path,"w") as f:
            json.dump(objectdict)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects , if it exist"""
        try:
            with open (FileStorage.__file_path) as f:
                objectdict = json.load(f)
                for o in objectdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
