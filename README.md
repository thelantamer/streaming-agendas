# thelantamer-streaming-agendas

This repo is where I keep all twitch and youtube streaming agendas, which includes topics, notes, and most notably links of the day (LOTD).

It's useful as a streamer, because these agendas are used for youtube uploads and come in handy when trying to remember specific links associated with topics covered in the stream.

# scripting

There are a few scripts in this repo related to automating the agenda generation process
These files are saved under \support-files folder
- newfile.py - python script that copies yesterday's agenda to a new file with today's date
- new-agenda.sh - bash script to launch the python script
- agenda-update-agent.plist - mac os x plist agent file, to use with launchctl to schedule to run once daily on local PC under user account context

scheduled via os x bash command:
  launchctl load ~/Library/LaunchAgents/agenda-update-agent.plist

  source: https://www.maketecheasier.com/use-launchd-run-scripts-on-schedule-macos/

# links
- twitch (https://twitch.tv/thelantamer/)
- youtube (https://www.youtube.com/thelantamer/)
- discord (https://discord.gg/BBSGPYH/)
- twitter (https://twitter.com/thelantamer/)
- instagram (https://www.instagram.com/thelantamer/)

# license
Licensed under the Creative Commons 4.0 License
