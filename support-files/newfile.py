# /usr/bin/python python
"""
Script to create today's streaming agenda file from yesterday's
works for Mac OS X or Linux for file
agenda-update.py
"""

# import modules
from datetime import date, timedelta
from shutil import copyfile

# filename for today's date
def get_filename_date_today():
    # Use current date to get a text file name.
    return str(date.today()) + ".twitch-stream-agenda.txt"

# filename for yesterday's date
def get_filename_date_yesterday():
    # Use current date to get a text file name for yesterday's date
    return str(date.today() - timedelta(days=1)) + ".twitch-stream-agenda.txt"

# Get full path for writing.
path = "/Users/qdd/Sync/git/streaming-agendas/"
print("PATH", path)

# display yesterday's filename
yesterdaysname = get_filename_date_yesterday()
print("YESTERDAYSNAME", yesterdaysname)

# display today's filename
todaysname = get_filename_date_today()
print("TODAYSNAME", todaysname)

# full source path
src = path + yesterdaysname
print("SRC", src)

# full destination path
dst = path + todaysname
print("DST", dst)

# copy operation from shutil module
copyfile(src,dst)
