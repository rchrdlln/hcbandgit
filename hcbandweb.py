#!/usr/bin/python
import time, urllib, os, random
# may 14 2015
# script to randomly generate 1980s hardcore band names and their demo tape titles
# create arrays of various categories of words and phrases
# create distinct methods of combining them using a random integer generator
# then use a random number gneerator to pick among methods
# would be best if could put info in database accessible via web
# not sure how to do that
# with small # items, can just put in array in script
# could maybe put in array in cgi or javascript also, although would be visible in source code?
#
# pseudocode
#
#to create method 1
# subpart 1 - create array of strings
# subpart 2 - create array of strings
# for subpart 1
# pick integer between [zero - ie first item in array] and [number of items in array]
# load this numbered item into variable 1
# for subpart 2
# pick integer between [zero - ie first item in array] and [number of items in array]
# load this numbered item into variable 2
# output = variable 1 + variable 2
#
# step 1
# how to create array of strings
# then create # arrays 
# - actually, thing to do wd be to create subarrays or lists then create multidimensional array containing them
# see http://www.i-programmer.info/programming/python/3942.html?start=1
# step 2
# python random # generator function - input is just # of items in array
# 
# step 3
# for [# of arrays], run the generator and get [# arrays] outputs named [output{# arrays]]
# step 4
# function to combine the string outputs into a phrase
# 
# print program title
print " " 
print "1980s HARDCORE BAND NAME GENERATOR"
print " " 
#usernumber = input ("ENTER A NUMBER BETWEEN 1 AND 10: ")
# print " " 
## this number is not used - just for fun
numrepeats = input ("HOW MANY BAND NAMES DO YOU WANT?: ")
# print " " 
#
# step 1
# decide string or list - 1125
# use lists - everyone uses list - will combine into 2D list
# initialize string list 1
# adjective - pejorative by conservative values
method1list1 = ['Wretched', 'Filthy', 'Scummy', 'Rotten', 'Dead', 'Crippled', 'Retarded', 'Damaged', 'Vandalized', 'Degraded', 'Obsolete', 'Radioactive', 'Infected', 'Nuclear', 'Toxic', 'Manipulated', 'Pat Robertsons', 'Tipper Gores', 'John Hinckleys', 'Jerry Falwells', 'Tammy Fayes', 'Diet', 'Junkie', 'Saccharine', 'Christian']
# testing 
# print "method1list1 is", method1list1
# 
# initialize string list 2
# noun - conservative value OR lame 70s/80s pop culture thing OR pejorative to punks
# eventually break out into separate arrays
method1list2 = ['Hippie', 'Respect', 'Honor', 'Pride', 'Patriotism', 'Valor', 'Religion', 'Authority', 'Family', 'History', 'Neighborhood', 'Jello', 'Twinkie', 'Winnebago', 'Rodeo', 'Hippie', 'Children', 'Grandpa', 'Cop', 'Priest', 'Youth', 'Militia', 'Battalion', 'Flag', 'Butthole', 'El Camino', 'Pinto', 'Jellybeans', 'Napalm', 'Ketchup', 'Cheeseburger']
# testing 
# print "method1list2 is", method1list2

# create 2D list
method1twodlist = [method1list1, method1list2]
# 
# testing 
# print "method1twodlist is", method1twodlist
#
# step 1 done 1145
#
# step 2 start 1145
# there is a python random # generator library
# get random number 1
# need # items in method1list1
# it's len(listname)
# create empty list
# the problem I had was creating the list after the for loop starts - it empties the list
print " " 
print "OK LET'S GO"
print " " 
time.sleep(2)
#
for num in range (0,numrepeats):
    outputlist = []
#
    for item in method1twodlist:
    
        randout = item[random.randint(0,(len(item) - 1))]
    
        outputlist.append(randout)
    # add a random plural every 6 to 8 times
    if random.randint(0,7) == 3:
        print " ".join(outputlist) + "s"
    else:
        print " ".join(outputlist)
       
    print " " 
#
print "DONE! FUCK RONALD REAGAN"
print " "
# one problem is that the random numbers are not nearly random enough - almost always 1 repeat in the first list and 1 in the second if you do over 10 names
# test to see if ever get 'Saccharine' or 'Cheeseburger' - the last items in each list
# try later deploying at pythonanywhere
# stop at 1330 pm