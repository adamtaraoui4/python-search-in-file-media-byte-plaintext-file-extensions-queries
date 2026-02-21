# -*- coding: utf-8 -*-
"""
Founder's firstnam : Adam
Founder's lastname : Taraoui
Founder's date of birth : 01/01/1990
Founder's place of birth : casablanca
Founder's company's name : zoom business intelligence
Founder's program's patent : GNU-GPG
Founder's program's description : 
Program to localize a file name of a directory name between 
a list of files and directories in a certain concrete directory or an abstract one.
If the query is found in a list of file or directories certain file is found, 
the found query is given in the certain line 
of the concrete directory path of the file.
"""
import os # importing the operating system
filesListSameNameAsQuery = [] # initialzing files name list with a name to fill it out
directoriesSameNameAsQuery = [] # initialzing directories name list with a name to fill it out
queryFound = False # setting up a boolean as query found not, to set it true if the query is found.
#'./' means current directory path, the loop is looking for all the '.txt' and '.log' extensions.
query = raw_input(str("Give a query name to look for : > ")) # selecting a query input
for root, dirs, files in os.walk('./'): # using os.walk function to walk through the given rootpath files and directories
    #print dirs
    #files
    for file in files: # looping through the files
        if query.strip() in file: # comparing the query name to the files names
            queryFound = True # setting query found is true
            full_path = os.path.abspath(os.path.join(root, file)) # making the variable full path of the file
            filesListSameNameAsQuery.append(full_path) # adding the file path to the directory
            #print "Full path appended : " + full_path
    for dircs in dirs: # looping through the files
        if query.strip() in dircs: # comparing the query name to the directories names
            queryFound = True # setting query found is true
            full_path = os.path.abspath(os.path.join(root, dircs)) # making the variable full path of the directory
            directoriesSameNameAsQuery.append(full_path)  # adding the directory path to the directory
            #print "Full path appended : " + full_path
if queryFound: # boolean(variable with true or false as choice) giving true if foldername, filename is found or some of the letters found in a certain foldername or filename.
    print ""
    print "The query was found : "
    print "----------------------"
    print "files :"
    print "----------------------"
    n = 1
    for x in filesListSameNameAsQuery: # printing files list
    	print str(n) + " : " + x
        n+=1
    print "----------------------"
    print "directories :"
    print "----------------------"
    n = 1
    for y in directoriesSameNameAsQuery: # printing directories list
    	print str(n) + " : " + x
        n+=1    	
else:
    print "The query was not found."
###########################################################
###########################################################
###########################################################
# Use minimum a letter to not get an error while looking for minimum a single character.
# place this file between files and folders where to look for to get an abstract path to the folder, a topmost place for a better tree structure without complications.
# Thank you in advance.
###########################################################
###########################################################
###########################################################

