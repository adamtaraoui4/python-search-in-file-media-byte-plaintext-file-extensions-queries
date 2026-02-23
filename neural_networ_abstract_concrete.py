# -*- coding:utf-8 -*-
import datetime
def addText(): # add text function/method
    queryFile = open('queryFile.txt','a') # we open a file to append, to it queries
    toAddQuery = str(raw_input("Add a certain query to search later :")) # input to put in a query
    queryFile.write(str(datetime.datetime.now()) + " : " + str(toAddQuery) + "\n") # write to files queries
    queryFile.close() # closing the file is very at the end of the use of the file
def searchText():  #search text function/method
    queryFile = open('queryFile.txt','r') # open the file for read
    queryFilesLines = queryFile.readlines() # we read the lines of the file
    result = [] # initialization of a result list
    toSearchQuery = str(raw_input("To search query now :")) # input to look for the query
    queryFound = False # initialize, the found query variable as boolean
    FoundInLine = 1 # we make line of the search queries
    for line in queryFilesLines: # loop through the lines of the file
        if toSearchQuery in line: # if the query is in readlines
            result.append("In file line : " + str(FoundInLine) + " line plaintext : " + str(line) + " query : " + str(toSearchQuery)) # we append to the query result list, the query and its line, if the query is found
            queryFound = True # if the query is found true
            FoundInLine+=1 # increment the line number of the query search
    if queryFound: # if the query is found
        print "The query was found :" # we print out a message
        for listLine in result: # loop through the result
            print listLine # print out list result
    else:
        print "The query was not found." # we print out another message
    queryFile.close() # closing the file is very at the end of the use of the file

#We may add functions as how much we looked for a query
#what we may do as manual or automatic 
#choices with a certain search of queries, 
#certain queries given, developing automatic 
#and manual functionality of the program 
#through functions, methods, fases of 
#development and file system(like database, 
#databse system build in this kind of program's 
#is very important, for that the program 
#may remember manual or automatic fases 
#of the program development) ->(program may 
#learn from itself)-> register everything 
#in filesystem build, databases and remembers 
#automatically fases of the program, has his own 
#agenda and for example working as a server.
def AddSearchCLIAbstractConcreteNeuralNetwork(): #CLI program
    print "--------------start CLI Network Program --------------"
    while 1:
        print "Options: "
        print "press 1. to add query"
        print "press 2. to search query"
        print "print ctrl+c(on windows, windows shortcut) to close the cli."
        request = str(raw_input("Give the request in : "))
        if request == str(1): # comparing to the choice, we select the function of the program
            addText()
        elif request == str(2): # comparing to the choice, we select the function of the program
            searchText()
        else:
             print "Error of choice : this choice doesn't exist."
    print "--------------end CLI Network Program --------------"
    
AddSearchCLIAbstractConcreteNeuralNetwork() # start the CLI method/function
    