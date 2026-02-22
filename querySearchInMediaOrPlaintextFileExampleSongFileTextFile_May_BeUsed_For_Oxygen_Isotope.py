# -*- coding: utf-8 -*-
"""
Firstname : Adam
Lastname : Taraoui
Date Of Birth : 01/01/1990
Place of birth : casablanca
Company's name : zoom business intelligence
Patent : GNU GPG
Program's descrisption : withdraw of 
a hash into plain from encryption 
to decryption from decryption to encryption.
Encryption/decryption of any hash.
"""
query = raw_input("Give a keyword to hash : ") # giving ascii, unicode characters as a test unit
xHashNumber = int(raw_input("Give a number of hash : ")) # giving a numer of a hash
def EncryptionOfHashQueryAddedToTheHashNumber(query, xHashNumber):
    # function to add the hash of unicode test unit to encrypt it
    # from the known characters.
    result = "" # set a string to fill out with hash
    for x in range(len(query)): # for loop to loop through the unicode characters and add the hash number of the unicode characters
        result += str(chr(ord(query[x])+xHashNumber)) # we add the encryption number, to the hash number
    return result # we return the encrypted string 
def DecryptionOfHashQuerySubstractedFromTheHashNumber(hashString, xHashNumber):
    # function to add the hash of unicode test unit to decrypt the encrypted hash
    # from the known characters.
    result = "" # set a string to fill out with hash
    for x in range(len(hashString)): # for loop to loop through the unicode characters and substract the hash number of the unicode characters
        result += str(chr(ord(hashString[x])-xHashNumber))
    return result # we return the decrypted string 
print "Primary plaintext to encrypt : " + query # method/function print the first given unicode characters
print "Print hashKey : " + str(xHashNumber) # method/function to print out the hash number
hashedQuery = EncryptionOfHashQueryAddedToTheHashNumber(query,xHashNumber) # encrypting the unicode characters
print "Encrypted query : " + hashedQuery # printing the unicode query after encryption
print "Decrypted query : " + DecryptionOfHashQuerySubstractedFromTheHashNumber(hashedQuery, xHashNumber) # printing the unicode query after decryption
"""
For oxygen isotope concern of forensics, 
It will about another extra useless hash 
will be a timestamp after happenings without 
correct value of information,
to unhash will be the isotope 
recovery of the timestamp of happenings 
itself, it will be about a useful information.
Beside oxygen Isotope for :
For plaintext latin,english,german 
languages 
files the are normally only 
255 beside all the 
unicode languages, example of 
(chinese, japanese, russian, Israeli)
, to encrypt to decrypt 
latin plaintext files
we use a simple dictionnary 
of latin languages when we meet 
a word of the dictionnaries 
we may test the decryption.
We may use for test unit, verbs 
(french : avoir, être), in 
four(4) languages, 
like english, Dutch, 
Italian, German.
"""


