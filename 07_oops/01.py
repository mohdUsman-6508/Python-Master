
class Car:
    
    total_car=0
    def __init__(self, brand, model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1
    
    # not very pythonic
    def get_brand(self):
        return self.__brand
    
    def set_brand(self,brand):
        self.__brand=brand
    
        
    def info(self):
        return f"{self.__brand} : {self.__model}"
    
    def fuel_type(self):
        print("Petrol or Diesal")
        
    @staticmethod
    def general_desc():
        print("Car is one of the fastest way of transport.")
        
    @property
    def model(self):
        return self.__model
    
    
    
class ElectricCar(Car):
    
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
        
    def fuel_type(self):
        print("Electric Charge")
    
    
    
first_tesla = ElectricCar("Tesla","Model Z","100 KWh")

# print(isinstance(first_tesla,Car))
# print(isinstance(first_tesla,ElectricCar))

# print(first_tesla.info())
# print(first_tesla.battery_size)
# first_tesla.fuel_type()


first_car = Car("Tata","Safari")
# print(first_car.get_brand(),":",first_car.model)
# print(first_car.info())
# first_car.set_brand("TATA")
# print(first_car.get_brand())
# first_car.fuel_type()

# print(Car.total_car)

# first_tesla.general_desc()
# first_tesla.general_desc()
# Car.general_desc()
  
# first_car.model="Sedan"
# print(first_car.model)
  
print(first_car.model)


class Battery:
    
    def battery_info(self):
        print("This is battery info.")
    
    def size(self):
        print("Battery size")

class Engine:
    
    def engine_info(self):
        print("This is engine info.")
    
    def size(self):
        print("Engine size")
    


class EV(Engine,Battery,Car):
    def __init__(self,brand,model):
        super().__init__(brand,model)
        

ev = EV("BYD","Phoenix")
ev.battery_info()
ev.engine_info()
print(ev.model)

#mro (EV->ENGINE->BATTERY->CAR->object)
ev.size()
ev.size()
print(EV.__mro__)