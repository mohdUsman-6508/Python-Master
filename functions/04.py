# function returning multiple values

# Create a function that returns both the area and the circumference of a circle given its radius

import math


def area_circumference(radius):
  area=(math.pi)*(radius**2)
  circumference=2*math.pi*radius


  return round(area,2),"%.4f"%circumference


area,cir=area_circumference(1)

print(f'Area:{area}, Circumference:{cir}')
a=11.22314

print(f'{a:.3f}')
