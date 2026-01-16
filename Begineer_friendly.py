# Write a program to find the area of the circle using two methods
# as well as we all know that the area of the circle becomes/is  = > pi * r * r


# (1) first method 
# here, user give the radius in input 
radius = int(input(" enter the radius of the circle  :" ))
# the area is of the circle is = > pi * r * r or 3.14 * radius * radius 

area = 3.14 * radius * radius
# print the area of the circle is

print(" The area is of the circle :" , area )
# output is let given to the radius of the circle is => 5 
# area is = > 78.53----


# (2)  second method
# we are write this second program to use module of (math)
# here we inlcude the import math module ( meaning is => to add math module )
import math 
# user enter the radius in own program

radius = float(input(" Enter the radius of the circle is :"))
# to find the area of the circle is
area = math.pi * radius * radius 
# print the area of the circle is
print(" The area is :" , area )

