class Wheel:
    def __init__(self, wtype, wspec = "winter"):
        self.wtype = wtype
        self.wspec = wspec

    def toString(self):
        return  ("Wheel Type: {}, Wheel Spec: {}".format(self.wtype, self.wspec))

class Engine:
    def __init__(self, etype = 2.4):
        self.etype = etype
    

class Car:
    def __init__(self, color = "grey", doors = 2, make = "coupe", model = "accord", seats = 5, etype = 2.4, wtype = "225/50R17", wspec = "winter" ):
        self.color = color
        self.doors = doors 
        self.make = make
        self.model = model
        self.seats = seats
        self.engine = Engine(etype)
        self.wheels = Wheel(wtype, wspec)

    def toString(self):
        return "Car Color {}".format (self.color + self.wheels.toString())
        

c1 = Car ()
print (c1.toString())


