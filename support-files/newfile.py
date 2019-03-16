# /usr/bin/python python
"""
Script to create today's streaming agenda file from yesterday's
works for Mac OS X or Linux for file
agenda-update.py
"""

### import modules ###

from datetime import date, timedelta
from shutil import copyfile
# regex library
import re
# import os to launch file open at tend
import os

### declare variables ###

# filename for today's date
def filename_today():
    # Use current date to get a text file name.
    return str(date.today()) + ".twitch-stream-agenda.txt"

# filename for yesterday's date
def filename_yesterday():
    # Use current date to get a text file name for yesterday's date
    return str(date.today() - timedelta(days=1)) + ".twitch-stream-agenda.txt"

# Path for writing.
path = "/Users/qdd/Sync/git/streaming-agendas/"

yesterdaysfile = path + filename_yesterday()
todaysfile = path + filename_today()

### Obtain previous vlog number, increment and add to new agenda file ###

# read first line from yesterday's file
filetext = open(yesterdaysfile)
yesterdaystext = filetext.readline()
filetext.close()

# create vlog number variable from regex search for numbers in first line
vlogday = (re.findall('\d+', yesterdaystext))

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

### Create new agenda file ###
# copy operation from shutil module
copyfile ( yesterdaysfile, todaysfile )

# update today's agenda with new title line
with open(todaysfile,'r+') as f: # open read-write
    f.readline() # read first line and ignore
    data=newline+f.read() #read newline and body of current file
    f.seek(0) # set cursor back to top
    f.write(data) # write data back to file


# open file in vs code
os.startfile(todaysfile)