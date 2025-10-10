

class Bus: #class
    def __init__(self, max_passengers): #constructor
        if max_passengers <=0:
            raise ValueError ('The bus is empty')
        self.max_passengers = max_passengers #attributes
        self.passengers = [] #empty list

    def load_passenger(self, passenger): #method #load the bus #validates the person instance
        if not isinstance(passenger, Person):
            raise TypeError("Only Person instances can board the bus")
        
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger) #ACTION add a passenger in passenger list
            print (f'{passenger.name} got on the Bus')
            return True
        else: 
            print('The Bus is 100% Capacity')
            return False

    def remove_passenger(self): #method #passenger got off
        if self.passengers:
            removed = self.passengers.pop(0) #action to remove the fist passenger that got in the Bus
            print(f'{removed.name} got off the Bus')
            return removed
        else:
            print('The Bus has capacity for new passengers')
            return None

class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Person ({self.name})'

p1 = Person('Adriana')
p2 = Person('Rodrigo')
p3 = Person('Mussy')

bus = Bus(2)
bus.load_passenger(p1)
bus.load_passenger(p2)
bus.load_passenger(p3)

bus.remove_passenger()
bus.load_passenger(p3)