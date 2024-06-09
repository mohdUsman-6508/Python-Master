
# bank ka registration form

class Car:

  # variable to store 
  total_car=0

  # constructor
  def __init__(self,brand,model):
    # self jodega connection
    # __private_variable--> accessible only within the class
    self.__brand=brand
    self.__model=model
    Car.total_car+=1

  def fullname(self):
    print(f'{self.__brand} {self.__model} is a wonderful car.')

# getter
  def get_brand(self):
    print(self.__brand)

# polymorphism
  def fuel_type(self):
    print("petrol or diesal")

# @decorators
# staticmethod 
#method only for the class not for the object, no need to use self keyword
  @staticmethod 
  def general_info():
      return "Cars are means of transportation."
  
  @property
  def model(self):
    return self.__model

  
    

  


# inheritance

class EV(Car):
  def __init__(self,brand,model,battery_size):
    self.battery_size=battery_size
    super().__init__(brand,model)
  
  # polymorphism
  # same function but different behaviour

  def fuel_type(self):
    print("Electric Charge")
  

car1 = Car("tata","safari")
# car1.fullname()
# print(car1.brand,car1.model)

ev1=EV("Tesla","Model S","100KWh")
# print(ev1.battery_size)
# ev1.fullname()
# # print(ev1.__brand)
# ev1.get_brand()
car2=Car("Rollce Royce","Phantom")

# ev1.fuel_type()
# car1.fuel_type()

# print(Car.total_car)
# car2.fuel_type()

# print(car1.general_info())
# print(Car.general_info())

# print(ev1.model)
# ev1.model="model v"
# print(ev1.model)


# isinstance

# print(isinstance(ev1,EV))
# print(isinstance(ev1,Car))


# multiple inheritence

class Battery:
  def power(self):
    return "Infinite Battery with super charge."

class Engine:
  def strength(self):
    return "Almost Infinite Strength with super intelligence"


class SuperCar(Car,Battery,Engine):
  def light(self):
    return "I am light"


osman=SuperCar("osman","Z")

print(osman.power())
print(osman.general_info())

print(osman.strength())
