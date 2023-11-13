class Flight:
    # method to create new flight with given capacity
    def __init__(self, flight_capacity):
        self.flight_capacity = flight_capacity
        self.passengers = []  # list of passengers in the flight
        # add a passenger to the flight
    def add_passenger(self, name, age):
        if len(self.passengers) < self.flight_capacity:
            self.passengers.append({'name': name, 'age': age})
            return 'added'
        else:
            return 'Flight is full'

flt_obj = Flight(2)
print(flt_obj.add_passenger('John', 32))
# Output: added
print(flt_obj.add_passenger('Jane', 45))
# Output: added
print(flt_obj.add_passenger('Alice', 18))
# Output: Flight is full