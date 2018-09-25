#
#Name: Maria Castillejo
#Student ID: 013827095
#Date (last modified): 9/24/2018
#
# Lab 0
# Section 13
# Purpose of Lab: To review and learn the basics of python
#
 
#weight float -> mars, jupiter str
#Return a person's mars and jupiter weight converted from their inputed earth weight.
def weight_on_planets():
   weight = float(input("What do you weigh on earth? "))
   mars = weight * 0.38
   jupiter = weight * 2.34
   print("\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds."%(mars,jupiter))   

if __name__ == '__main__':
   weight_on_planets()
