# thelantamer-streaming-agendas

This repo is where I will start keeping all streaming agendas, which includes topics discussed on each stream and LOTD (Links of the Day).

For viewers, these repos can by synced and referenced during a stream to follow along with any links.

It's useful as a streamer, because these agendas are used for youtube uploads and come in handy when trying to remember specific links associated with topics covered in the stream.

- SCRIPTING -
There are a few scripts in this repo related to automating the agenda process
These files are saved under \support-files folder

newfile.py - python script that copies yesterday's agenda to a new file with today's date

new-agenda.sh - bash script to launch the python script

agenda-update-agent.plist - mac os x plist agent file, to use with launchctl to schedule to run once daily on local PC under user account context

    scheduled via os x bash command:
        launchctl load ~/Library/LaunchAgents/agenda-update-agent.plist

    source: https://www.maketecheasier.com/use-launchd-run-scripts-on-schedule-macos/