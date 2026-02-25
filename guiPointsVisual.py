# -*- coding: utf-8 -*-
"""
copyright all rights reserved
Founder's firstname : adam
Founder's lastname : taraoui
Founder's moroccan id number : AB.64.52.76
Founder's belgian id number : 90.01.01.475.34
Founder's company's name : zoom business intelligence
Founder's place of birth : casablanca
Founder's date of birth : 01/01/90
Program patent : GNU-GPG
Description : a red dot detected in canvas 
by the previous matrix negative temperature 
points, as a graphic interface 
-> neutralized in white points, green points.
"""
import turtle
import time

# Set up the screen
screen = turtle.Screen()
bgColor = "white"
screen.bgcolor(bgColor)

# Create a turtle object (your "pen")
t = turtle.Turtle()
t.penup()
t.hideturtle() # Optional: hides the arrow shape

# Draw a dot: dot(size, color)
# Size is the diameter in pixels
"""
Modular one time.
"""
#------------------------
for x in range(4):
    t.forward(40)
    t.right(90)
    t.dot(20, "red")

time.sleep(1)
    
for x in range(4):
    t.forward(40)
    t.right(90)
    t.dot(20, bgColor)

time.sleep(1)
    
for x in range(4):
    t.forward(40)
    t.right(90)
    t.dot(20, "green")  
#------------------------
"""
Server working forever setting data, 
and neutralizing negative data forever.
Collecting data analysis will be through 
adding a log file, adding to it data
and rendering it,  for higher accuracy, 
efficiency of source points and 
their formula's provenance, destination, 
manifestation, impact, better neutralization 
with impact -> a safe harbour defense system.
"""
while 1:
    t.forward(40)
    t.right(90)
    t.dot(20, "red")
    
    #time.sleep(1)
    
    t.forward(40)
    t.right(90)
    t.dot(20, bgColor)
    
    #time.sleep(1)
    
    t.forward(40)
    t.right(90)
    t.dot(20, "green")      
"""
In data analysis, 
in our case the pen will be 
the source of the colour.
In real life situations, 
it will be a source of energy 
detected, localized by a temperature sensor.
(you may set an extra file to log, 
register data for higher level data 
analysis, through a 3 dimensional temperature sensor)
with previous diamond-v.0.4-python2.7 from mr. adam taraoui,
moroccan id number : AB.64.52.76
belgian id number : 90.01.01.475.34
"""
# Keep the window open until a user clicks on it
screen.exitonclick()