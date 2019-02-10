class Trip:
    
    _all = []

    def __init__(self, start, destination, driver):
        self._start = start
        self._destination = destination
        self._driver = driver
        Trip.add_trip(self)
	    # remember to associate a trip with a driver
    
    @classmethod
    def add_trip(cls, trip_instance):
        cls._all.append(trip_instance)
    
    @property
    def start(self):
        return self._start
    @property
    def destination(self):
        return self._destination
    
    @property
    def driver(self):
        return self._driver
    
    @start.setter
    def start(self, new_start):
        self._start = new_start
    @destination.setter
    def destination(self, new_destination):
        self._destination = new_destination
    @driver.setter
    def driver(self, new_driver):
        self._driver = new_driver
    
    @classmethod
    def get_trips(cls):
        return cls._all
    