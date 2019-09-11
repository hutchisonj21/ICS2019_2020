"""

This program converts Fahrenheit to Celsius, acres to barns,
and draws a polygon all based on user input

@author Jayden Hutchison
@version 1.0
@since 9/8/19

"""

import turtle


#This method converts Fahrenheit to Celsius
def fahrenheitToCelsius(fahrenheit):
	celsius = (fahrenheit - 32) * 5/9
	print(str(fahrenheit) + " degrees Fahrenheit is " + str(celsius) + " degrees in Celsius.")


#This method converts acres to barns
def acresToBarns(acres):
	barns = acres * 4.047e+31
	print(str(acres) + " acres is " + str(barns) + " barns.")


#This method draws a polygon based on a user input number of sides
def drawPolygon(sides):
	outerAngle = 360/sides
	jim = turtle.Turtle()
	n = sides
	while (n > 0):
		jim.forward(50)
		jim.left(outerAngle)
		jim.forward(50)
		n-=1
	
	screen=jim.getscreen()
	screen.mainloop()

#asks for a number in fahrenheit to convert to celsius
fahrenheit = int(input("Enter a value of degrees in fahrenheit that you would like converted to celsius: "))

fahrenheitToCelsius(fahrenheit)

#asks for a number in acres to convert to barns
acres = int(input("Give me an amount of acres and I will convert it to barns: "))

acresToBarns(acres)

#asks for a number of sides to draw a regular polygon
sides = int(input("Give me a number of sides (larger than two) and I will draw a polygon with that number of sides (Note: do not enter a huge number for the sake of time): "))

drawPolygon(sides)
