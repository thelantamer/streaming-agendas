# /usr/bin/python python
"""
Script to create today's streaming agenda file from yesterday's
works for Mac OS X or Linux for file
agenda-update.py
"""

# import modules
from datetime import date, timedelta
from shutil import copyfile

# setup variables

# filename for today's date
def get_filename_date_today():
    # Use current date to get a text file name.
    return str(date.today()) + ".twitch-stream-agenda.txt"

# filename for yesterday's date
def get_filename_date_yesterday():
    # Use current date to get a text file name for yesterday's date
    return str(date.today() - timedelta(days=1)) + ".twitch-stream-agenda.txt"

# Get full path for writing
path = "/Users/qdd/Google Drive/git/streaming-agendas/"

# full source path
src = path + get_filename_date_yesterday

# full destination path
dst = path + get_filename_date_today

# copy operation from shutil module
copyfile(src,dst)