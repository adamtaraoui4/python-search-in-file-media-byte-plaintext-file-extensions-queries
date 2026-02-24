# -*- coding: utf-8 -*-
#Founder's firstname : adam
#Founder's lastname : taraoui
#Fouder's company's name : zoom business intelligence
#Name of the program : Antikythera clock
#Patent : GNU-GPG
#Description : in the Antikythera world,
# 66 seconds for 1 minute, 60 minutes for one hour,
# 24 hours for 1 day.
import time # importing time's tick second tick
def main(): # defining a main function to use
    xDays = 0 # stands for the days, untill now
    xHours = 0 # stands for the hours, untill now
    xMinutes = 0 # stands for the minutes, untill now
    xSeconds = 0 # stands for the seconds, untill now
    while 1: # a forever loop
            for hours in range(24): # for loop stands for 24 hours
                for minutes in range(60):  # for loop stands for 60 minutes
                    for seconds in range(66): # for loop stands for 66 seconds, in antikythera clock the minute has 66 seconds
                        time.sleep(1) # second tick
                        xSeconds+=1 # incrementing seconds by one
                        print "Days : " + str(xDays) + " Hours : " + str(xHours) + " Minutes : " + str(xMinutes) + " Seconds : " + str(xSeconds) # printing the clock every second
                        print "Press shortcut ctrl+c to exit the program." # closing the CLI program, by the shortcut ctrl+c on windows
                    xMinutes+=1 # after 66 seconds, incrementing the minutes by 1
                    xSeconds=0 # setting the seconds to 0
                xHours+=1 # after 60 minutes, incrementing the hours by 1
                xMinutes=0 # setting the minutes to 0
            xDays+=1 # after 24 hours, incrementing the days by 1
            xHours=0 # setting the hours to 0
main() # calling the main function/method to start use the program.
 
         
    