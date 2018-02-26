from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print "Good morning, Dileesh. The calculator is starting up..."
print "The current time is: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)
sleep(1)
hint = "Units \nExiting..."
option = raw_input("Enter C for Circle or T for Triangle: ")
option.upper()
if option == 'C':
    radius = float(raw_input("Please input the radius: "))
    area = pi * radius**2
    print "Calculating Area........"
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
elif option == 'T':
    base = float(raw_input("Please input the base of the Triangle: "))
    height = float(raw_input("Please input the height of the Triangle: "))
    area = (0.5)*base*height
    sleep(1)
    print ("Area: %.2f \n%s" % (area, hint))
else:
    print "Error! That input is Incorrect! The program will now exit...!"