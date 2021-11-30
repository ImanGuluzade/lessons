


class Cars:
   def __init__(self, inp_engine=2.0, inp_gass="petrol", inp_transmission="manual", door=4, ban="sedan"):
    self.transmission, self.engine, self.gass, self.door, self.ban = inp_transmission, inp_engine, inp_gass, door, ban
  
    car_door = lambda self: print("Every cars has dors. My car has "  + str(self.door) + " doors")
    car_ban = lambda self, e: "My car ban is: " + str(e)

    __str__ = lambda self: "Engine: " + str(self.engine) + ",\tGass:  " + str(self.gass) + ",\tTransmisson: " + str(self.transmission)

vag_car = Cars()
imn_car = Cars()
