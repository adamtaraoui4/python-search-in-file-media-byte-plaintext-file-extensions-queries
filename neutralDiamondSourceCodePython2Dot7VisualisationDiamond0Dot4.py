# -*- coding: utf-8 -*-
"""
    Founder's firstname : adam
    Founder's lastname : taraoui
    Founder's nationality : moroccan
    Founder's moroccan id number : AB.64.52.76
    Founder's belgian id number : 90.01.01.475.34
    Founder's company's name : zoom business intelligence
    Founder's place of birth : casablanca
    Founder's date of birth : 01/01/90
    Program's patent  : GNU-GPG
    Program's programming language : python-2.7
    Program's description getting in 3d dimensional 
    canvas in space temperature points and neutralizing them 
    by an absolute coldness temperature found 
    in space by a temperature sensor, 
    as a neutralizing procedure.
"""
import time
import datetime
import random
print "---------------------------"
print "Program start : >>> "
print "---------------------------"
aMatrixExampleVariable = [[[x for x in range(3)] for x in range(3)] for x in range(3)]
logFileNameAndExtensionVariable = "logFile.txt"
logFileDocumentVariable = open(logFileNameAndExtensionVariable, 'a')
print "---------------------------"
print "Timestamp : date and time(from current hardware machine) : \n" + str(datetime.datetime.now())
print "---------------------------"
print "Print of the usual 3 dimensional matrix :"
print "---------------------------"
"""
Methods
------------------------------------------------
------------------------------------------------
------------------------------------------------
"""
def printMatrix(matrixSetVariable):
    """
    Method to print the matrix set.
    """
    for x in matrixSetVariable:
        print x
def setOfRandomTemperatureSimulatorMethod(matrixSetVariable):
    """
    Method to set random numbers as simulation 
    of temperature points.
    """
    """
    -1 negative value, 
    0 yet neutralized, 
    2 neutralized and cold behaviour
    extern coldness value, we may set -67
    """
    randomListNumberVariable = [-1,2,0]
    randomChoiceNumberVariable = None
    """
    Setting a random number to track out, 
    later by this simulator and neutralize.
    """
    randomChoiceNumberVariable = random.randint(0,len(randomListNumberVariable)-1)
    #print randomListNumberVariable[randomChoiceNumberVariable]
    for t in range(len(matrixSetVariable)):
        randomChoiceNumberVariable = random.randint(0,len(randomListNumberVariable)-1)
        for b in range(len(matrixSetVariable)):
            randomChoiceNumberVariable = random.randint(0,len(randomListNumberVariable)-1)
            for c in range(len(matrixSetVariable)):
                randomChoiceNumberVariable = random.randint(0,len(randomListNumberVariable)-1)
                matrixSetVariable[t][b][c] = randomListNumberVariable[randomChoiceNumberVariable]
            randomChoiceNumberVariable = None
def neutralizingPointsMethod(matrixSetVariable, valueOfNeutralizationVariable, logFileLocal):
    """
    Method to neutralize the unussual temperature 
    in the matrixSetVariable by a cold point got 
    by a temperature sensor.
    """
    """
    looping the matrix from each index, looping through the matrix
    """
    for t in range(len(matrixSetVariable)):
        for b in range(len(matrixSetVariable)):
            for c in range(len(matrixSetVariable)):
                if matrixSetVariable[t][b][c] == -1:
                    """
                    writing in the logFileDocument 
                    the timestamp the matrix indexes 
                    of the negative point, in this simulator 
                    we just use -1 as value.
                    """
                    logFileLocal.write(str(datetime.datetime.now()) + " " + str(t) + " " + str(b) + " " + str(c) + " " + " negative \n")
                    """
                    Neutralizing the localized point 
                    to the neutralization value.
                    """
                    matrixSetVariable[t][b][c] = valueOfNeutralizationVariable
def printLogFileLinesMethod(logFileDocumentNameAndExtension):
    """
    Method to print out the simulator logFile data.
    """
    openLogFileDocumentToRead = open(logFileDocumentNameAndExtension, 'r')
    logFileReadLines = openLogFileDocumentToRead.readlines()
    print "logFile begin print > "
    for logLine in logFileReadLines:
        print logLine
    print "logFile end print."
    openLogFileDocumentToRead.close()
"""
Simulator
------------------------------------------------
------------------------------------------------
s
"""
try:
    print "Simulator begin :"
    """
    A simulator of 10 times numbers 
    with an offset of 1 second by set.
    """
    for z in range(10):
        """
        Using the methods
        """
        print "---------------------------"
        print aMatrixExampleVariable
        print "Print printMatrix method :"
        printMatrix(aMatrixExampleVariable)
        print "---------------------------"
        print "Print setOfRandomTemperatureSimulatorMethod loading..."
        setOfRandomTemperatureSimulatorMethod(aMatrixExampleVariable)
        print "---------------------------"
        print "Print printMatrix method"
        printMatrix(aMatrixExampleVariable)
        print "---------------------------"
        """
        valueOfColdnessInSpace may be 
        in study as a value of 99 minus
        99 as just a number to change 
        with the coldest point value 
        found by a temperature sensor.  
        We may take a variable valueOfNeutralization = 99.
        99 as just a choosen number in our simulator.                  
        """
        print "Method to neutralize loading..." 
        neutralizingPointsMethod(aMatrixExampleVariable,99,logFileDocumentVariable)
        print "---------------------------"
        print "Print printMatrix method :"
        printMatrix(aMatrixExampleVariable)
        print "---------------------------"
        time.sleep(1)
        """
        A simulator of always running by 
        setting a while 1: loop as controle 
        and neutralization tour going forever 
        without stop without a use of 
        an offset of seconds.    
        """
    while 1:
        """
        Using the methods
        """
        print "---------------------------"
        print aMatrixExampleVariable
        print "Print printMatrix method :"
        printMatrix(aMatrixExampleVariable)
        print "---------------------------"
        print "Print setOfRandomTemperatureSimulatorMethod loading..."
        setOfRandomTemperatureSimulatorMethod(aMatrixExampleVariable)
        print "---------------------------"
        print "Print printMatrix method"
        printMatrix(aMatrixExampleVariable)
        print "---------------------------"
        """
        valueOfColdnessInSpace may be 
        in study as a value of 99 minus
        99 as just a number to change 
        with the coldest point value 
        found by a temperature sensor.  
        We may take a variable valueOfNeutralization = 99.
        99 as just a choosen number in our simulator.                  
        """
        print "Method to neutralize loading..." 
        neutralizingPointsMethod(aMatrixExampleVariable,99,logFileDocumentVariable)
        print "---------------------------"
        print "Print printMatrix method :"
        printMatrix(aMatrixExampleVariable)
        print "---------------------------"
        """
        Adding data to text files 
        could be useful for data analisys
        about points in perimeter, and movement 
        of damage, and a method to centralize the sources.
        style of a server always working.
        """
        """
        we may print the logFile 
        in extern documents, 
        using documents of the same 
        document splitted out for easy 
        and fast read by the program 
        datak(less time and efficient accuracy in execution).
        """
except Exception as e:
    print "A not indexed exception occured."
"""
-----------------------------------------
-----------------------------------------
-----------------------------------------
"""
"""
closing the logFile is very important 
after each use in the program, 
otherwise we may lose data.
"""
logFileDocumentVariable.close()
"""
If we want to print the logFileDocument, 
we may print it after 10 times 
execution, each after one second.
"""
"""
Using the method printLogFileLinesMethod 
to read data, after closing the file from the append.
"""
printLogFileLinesMethod(logFileDocumentVariable)
"""
We use other programs to read the 
logFile data for higher speed, 
efficiency and accuracy.
"""
print "Program finished." 