# remeber to import the trip class here
from trip import Trip

class Driver:
    
    _alldrivers = []
   
    @classmethod
    def add_driver(cls, driver_instance):
        cls._alldrivers.append(driver_instance)
        
    @classmethod
    def get_alldrivers(cls):
        return cls._alldrivers
    
    def __init__(self, name):
        self._name = name
        Driver.add_driver(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    def my_trips(self):
        result = [tri for tri in Trip._all if self._name == tri.driver.name]
        return result
       
    def my_trip_summaries(self):
        result = []
        for tri in self.my_trips():
            result.append("{} to {}".format(tri.start,tri.destination))
        return result
