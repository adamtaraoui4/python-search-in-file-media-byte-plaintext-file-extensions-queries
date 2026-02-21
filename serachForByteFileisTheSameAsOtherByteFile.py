# -*- coding: utf-8 -*-
"""
Founder's firstnam : Adam
Founder's lastname : Taraoui
Founder's date of birth : 01/01/1990
Founder's place of birth : casablanca
Founder's company's name : zoom business intelligence
Founder's program's patent : GNU-GPG
Founder's program's description : 
Program to localize a media(byte) query between 
files in a certain concrete directory or an abstract one.
If the query in a certain file is found, 
the found query is given in the certain line 
of the concrete directory path of the file
file byte the same as another byte file.
(a file of a song or a picture to find it back in a certain directory)
"""
import os # importing the operating system
filesEndsWithDotTxtOrDotLogExtension = [] # initialzing a list with a name to fill it out
#'./' means current directory path, the loop is looking for all the '.txt' and '.log' extensions.
for root, dirs, files in os.walk('./'): # using os.walk function to walk through the given rootpath files and directories
    for file in files: # looping through the files
        if file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.jpg') or file.endswith('.gif'): # condition, if the files endswith '.txt', '.log'
            # Use os.path.join to get the full path
            full_path = os.path.abspath(os.path.join(root, file)) # making the variable full path of the directory
            filesEndsWithDotTxtOrDotLogExtension.append(full_path) 
            #print "Full path appended : " + full_path
query = raw_input(str("Give an input(file) to look for in  byte files in a certain path : > ")) # selecting a query input
queryReadedFile = open(query,'rb') # read the files already selected by the previous lines
queryReadedFilesReadlines = readedFile.read() #reading the lines of the files
queryFound = False # setting up a boolean as query found not, to set it true if the query is found.
queryFoundList = [] # initializing an empty list to fill up the list
for xFile in filesEndsWithDotTxtOrDotLogExtension: # looping through the files
    readedFile = open(xFile,'rb') # read the files already selected by the previous lines
    readedFilesReadlines = readedFile.read() #reading the lines of the files
    lineNumber = 0 # initializing the line numbers to zero
    for xLine in readedFilesReadlines: # looping every line of every line ang looking for the query
        if queryReadedFilesReadlines in xLine: # condition if the query is found in the line
            queryFound = True # setting up the variable as queryFound True
            queryFoundList.append("fileName : " + str(xFile) + " LineNumber : " + str(lineNumber) + " query found.") # appending to already an initialized list the line of the file found in query.
        lineNumber+=1 # incrementing the line numbers
    lineNumber = 0 # initialization of a lineNumber to zero
    readedFile.close() # close the file
if queryFound: # if the query is already found just one time
    print "Query found in : " # print on the screen the query is found
    n = 1
    for x in queryFoundList: # printing the list of the files where the query is found at
	print str(n) + " : " + x
    	n+=1
else: # elsewhere from the last condition
    print "Query not found" # printing out, the query was not found
###########################################################
###########################################################
###########################################################

###########################################################
###########################################################
###########################################################

