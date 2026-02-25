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
#An example real life example : After a search 
#of plaintext seinding a processus command 
#automatically to send an email, get manufacturer, 
#get a job/work done without any extra third party help, 
#being fully independent in the job.
#On Python : like webapp working with Flask as a server
#(or a python CLI application working forever as a serve, 
#or any other programming language having the same 
#options who may work as a server), 
#checking every employee if his coming to the his job/work 
#in time, the program described as manufacture, paying 
#the employees in time, delegated by all the tasks of 
#feedbacks by for example an email system, looking for more 
#employees if it's needed and recruting them, paying the taxes 
#at the end of the year or delegating it to the correct employee 
#and always checking back the work is done, by failure of 
#insolvency looking for the best options for the manufacture 
#to get back solvency by changing extra valuta of the prices or 
#selling the manufacture in time for another third party company 
#or own company without debts for lesser failure of incolvency 
#problems.
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
    