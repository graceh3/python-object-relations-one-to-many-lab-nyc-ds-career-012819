# import car class here
from car import Car

class Owner:
    
    _allowners=[]
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @classmethod
    def add_owner(cls, owner_instance):
        cls._allowners.append(owner_instance)
    
    @classmethod
    def get_allowners(cls):
        return cls._allowners
    
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    
    @name.setter
    def name(self, new_name):
        self._name = new_name  
    @age.setter
    def age(self, new_age):
        self._age = new_age

    def find_my_cars(self):
        makes = []
        models = []
        for car in Car._all:
            if self._name == car.owner.name:
                makes.append(car.make)
                models.append(car.model)
        result = ["{} {}".format(make_, model_) for make_, model_ in zip(makes, models)]
        return result
