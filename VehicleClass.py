class Vehicle:
    def __init__(self, wheels = 4, esize = None, doors = None, length = None, height = None, seats = 5, model = None):
        self.wheels = wheels
        self.esize = esize
        self.doors = doors
        self.length = length
        self.height = height
        self.seats = seats
        self.model = model


    def toString (self):
        v = "This model is a {}.\n".format (self.model)
        v += "The engine size is a {}.\n".format (self.esize)
        v += "There are {} doors.\n".format (self.doors)
        v += "This vehicle is {} meters long.\n".format (self.length)
        v += "This vehicle is {} meters high.\n".format (self.height)
        v += "This vehicle can seat {} people.\n".format (self.seats)
        v += "This vehicle comes with {} wheels.\n".format (self.wheels)
        return v

class Sedan (Vehicle):
    def __init__(self, esize = 2.4, doors = 4, length = 4.9, height = 1.5, model = "Sedan"):
        super().__init__()
        self.esize = esize
        self.doors = doors
        self.length = length
        self.height = height
        self.model = model

    def getEsize (self):
        return self.esize

    def getLength (self):
        return self.length

    def getHeight (self):
        return self.height

    
class Suv (Vehicle):
    def __init__(self, esize = 2.5, doors = 4, length = 4.6, height = 1.8, hatch = True, model = "SUV"):
        super().__init__()
        self.esize = esize
        self.doors = doors
        self.length = length
        self.height = height
        self.hatch = hatch
        self.model = model


class Compact (Vehicle):
    def __init__(self, esize = 1.8, doors = 4, length = 4.4, height = 1.5, model = "Compact"):
        super().__init__()
        self.esize = esize
        self.doors = doors
        self.length = length
        self.height = height
        self.model = model


class Coupe (Vehicle):
    def __init__(self, esize = 2.4, doors = 2, length = 4.9, height = 1.5, model = "Coupe"):
        super().__init__()
        self.esize = esize
        self.doors = doors
        self.length = length
        self.height = height
        self.model = model


s1 = Sedan ()
c1 = Coupe ()
c2 = Compact ()

print (c1.toString())
print (s1.toString())
print (c2.toString())