#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def parse(arg):
     curly_braces = re.search(r"\{(.*?)\}", arg)
     brackets = re.search(r"\[(.*?)\]", arg)
     if curly_braces is None:
          if brackets is None:
               return [i.strip(",") for i in split(arg)]
          else:
               lexer = split(arg[:brackets.span()[0]])
               ret1 = [i.strip(",") for i in lexer]
               ret1.append(brackets.group)
               return ret1
     else:
          lexer = split(arg[:curly_braces.span()[0]])
          ret1 = [i.strp("") for i in lexer]
          ret1.append(curly_braces.group)
          ret1


class HBNBCommand(cmd.Cmd):
    """ 
    Defines the  command interpreter
    Attributes:
        prompt (str):the command prompt
    """

    prompt = "(hbnb)"
    __classes = {
         "BaseModel",
         "User",
         "State"
         "City"
         "Place"
         "Amenity"
         "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior when invalid input is entered throught the cmd module"""
        arg_dict = {
            "all":     self.do_all,
            "show":    self.do_show,
            "destory": self.do_destroy,
            "count":   self.do_count,
            "update":  self.do_update

        }
        match = re.search(r"\.",arg)
        if match is not None:
             arg1  = [arg[:match.span()[0]], arg[match.span()[1]:]]
             match = re.search(r"\((.?)\)", arg1[1])

             if match is not None:
                   command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                   if command[0] in arg_dict.keys():
                         call = "{} {}".format(arg1[0],command[1])
                         return arg_dict[command[0]](call)
                   print("*** Unknown command: {}".format(arg))
                   return False
             
    
    def do_quit(self, arg):
         """Exiting the program"""
         return True
    
    def do_EOF(self,arg):
         """EOF Signal to exit the program"""
         print("")
         return True

    def do_create(self, arg):
         """Create: create a new instance of a class"""
         arg1 = parse(arg)
         if len(arg1) == 0:
              print("** class name missing")
         elif arg1[0] not in HBNBCommand.__classes:
              print("** class doesn't exist")
         else:
              print(eval(arg1[0])().id)
              storage.save()


    def do_show(self,arg):
         """Show class ,id Display the string
            representation of a class instance of a given id
         """
         arg1 = parse(arg)
         objdict = storage.all()
         if len(arg1) == 0:
              print("** class name missing **")
         elif arg1[0] not in HBNBCommand.__classes:
              print("** class doesn't exist")
         elif len(arg1) == 1:
              print("** instance id missing**")
         elif"{}{}".format(arg1[0], arg1[1]) not in objdict:
              print("** no instance found **")
         else:
              print(objdict["{}.{}".format(arg1[0],arg[1])])

                

    def do_all(self,arg):
        """
            all the class object
            show all the string representation of all the instance
            of a given class.

            If no class is specified, display all instaniate objects
        """
        arg1 = parse(arg)
        if len(arg1) > 0 and arg1[0] not in HBNBCommand.__classes:
            print("** class doen't exist **")
        else:
            obj1 = []
            for obj in storage.all().values():
                if len(arg1) > 0 and arg1[0] == obj1.__class__.__name__:
                    obj1.append(obj.__srtr__())
                elif len(arg1) == 0:
                    obj1.append(obj.__str())
            print(obj1)

    def do_destroy(self, arg):
         """
            destroy class id 
            Delete a class instance of a given id
         """  
         arg1 = parse(arg)
         objdict = storage.all()
         if len(arg1) == 0:
              print("** class name missing **")
         elif arg1[0] not in HBNBCommand.__classes:
              print("** class doesn't exist")
         elif len(arg1) == 1:
              print("** instance id missing**")
         elif"{}{}".format(arg1[0], arg1[1]) not in objdict.keys():
              print("** no instance found **")
         else:
              del objdict["{}.{}".format(arg1[0],arg[1])]
              storage.save()
    
    def do_count(self,arg):
         """Count <class> Retrieve the  number of instance of a given class"""
         arg1 = parse(arg)
         count = 0
         for obj in storage.all().values():
              if arg1[0] == obj.__class__.__name__:
                   count +=1
         print(count)

    def do_update(self,arg):
         """Update class object 
            update class id attribute_name and attribute_value
         """
         arg1 = parse(arg)
         objdict = storage.all()         
         if len(arg1) == 0:
              print("** class name missing **")
              return False
         if arg1[0] not in HBNBCommand.__classes:
              print("** class doesn't exist **")
              return False
         if len(arg1) == 1:
              print("** instance id missing **")
              return False
         if "{}.{}".format(arg1[0],arg1[1] not in objdict.keys()):
              print("** no instance found **")
              return False
         if len(arg1) == 2:
              print(" ** attribute name missing ***")
              return False
         if len(arg1) == 3:
              try:
                   type(eval(arg1[2])) != dict

              except NameError:
                   print("** value missing **")
                   return False
         
         if len(arg1) == 4:
              obj = objdict["{}.{}".format(arg1[0],arg1[1])]
              if arg1[2] in obj.__class__.__dict__.keys():
                   valtype = type(obj.__class__.__dict__[arg1[2]])
                   obj.__dict__[arg1[2]] = valtype(arg1[3])
              else: 
                  obj.__dict__[arg1[2]] = arg1[3]

         elif type(eval(arg1[2])) == dict:
              obj = objdict["{}.{}".format(arg1[0],arg1[1])]
              for key,value in eval(arg1[2]).items():
                   if (key in obj.__class__.__dict__.keys() and type(obj.__class__.__dict__[key]) in {str,int,float}):
                        valtype = type(obj.__class__.__dict__[key])
                        obj.__dict__[key] = valtype(value)

                   else:
                        obj.__dict__[key] = value
         storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
