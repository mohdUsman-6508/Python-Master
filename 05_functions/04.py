
import math

def calcAreaAndCircum(radius):
  area=round(math.pi*(radius**2),3)
  circumference=round(2*math.pi*radius,3)
  circle_stats={"a":area,"c":circumference}
  
  return circle_stats

radius = float(input("Enter radius(cm): "))
calculated_vals=calcAreaAndCircum(radius)
print(calculated_vals['a'])

print(str.format("Area: {}, Circumference: {}" , calculated_vals['a'],calculated_vals['c']))