# /usr/bin/python python
"""
Script to create today's streaming agenda file from yesterday's
works for Mac OS X or Linux
agenda-update.py
"""

### import modules ###

# modules to get current date and time
from datetime import date, timedelta
# os copyfile function
from shutil import copyfile
# regex library for searching within file
import re
# check if file exists
import os.path


# variable for working path
path = "/Users/qdd/Sync/git/streaming-agendas/"
filestem = ".twitch-stream-agenda.txt"

### file naming variables based on dates ###
# filename for today's date
def newfile():
    # Use current date to get a text file name.
    return str(path + str(date.today()) + filestem)

def lastfile():
    return str(path + str(date.today() - timedelta(days=count)) + filestem)

count = 1
while os.path.isfile(lastfile()) == False:
    count+=1

copyfile (lastfile(),newfile())

### Obtain previous vlog number in file, increment and add to new agenda file ###
# read first line from yesterday's file
filetext = open(lastfile())
agendaheaderline = filetext.readline()
filetext.close()

# create vlog number variable from regex search for numbers in first line
vlogday = (re.findall('\d+', agendaheaderline))
# resulting string is a list, join into a single string variable
vlogday = "".join(vlogday)
# convert string variable to integer
vlogday = int(vlogday)
# new variable for next vlog number
newvlogday = (vlogday + 1)
# string for new firstline in new agenda
newlinepart1 = "day "
newlinepart2 = " - TITLE \n"
newline = newlinepart1 + str(newvlogday) + newlinepart2

# update today's agenda with new title line
with open(newfile(),'r+') as f: # open read-write
    f.readline() # read first line and ignore
    data=newline+f.read() #read newline and body of current file
    f.seek(0) # set cursor back to top
    f.write(data) # write data back to file

# EOF