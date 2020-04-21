# SongTitleParser
A short python script that scrapes the song title out of supported media players and outputs them into text files.
The purpose of this script was to have a relatively easy way to display song titles onto OBS (Open Broadcast Software) without much bloat on my current configuration.

Effectively looks for running applications with specific titles (namely "VLC" and "Spotify") and will output their current window title that contains a song to an applications specific text file.
This may not be the app for you if you are looking for a broad range of supported devices or support for the web varient of Spotify (though I plan to look into support soon...), however there are already many similar applications that provide further support in a more user friendly way.
If, however, you just want a lightweight app for your local media with a minimal feature set, than this might be worth a try!

Currently, the following media players are supported:
1. VLC
2. Spotify - Desktop client only

## Requirements
1. Python3
2. Windows

## Instructions
1. Download or clone this project and extract it
2. Locate - FindTitle.py
3. Run the script - Python FindTitle.py

* A folder will be generated in the directory this script was run containing .txt files named after supported media players
* The script will continuously be looking for any of these supported media players running, and if one is detect with a playing song, that song's title should be written in the .txt file of whichever media player was playing it
* These .txt will be cleared when the application is shut down

## Limitations
1. Currently has only been tested on Windows 10 through utilization of the win32gui module. It is unlikely to currently work on Linux but I am currently planning a port
2. Spotify must not be playing a song when this application is started in order for the script to correctly track its GUI
3. If a different application contains the name of one of these supported media players and is running, incorrect results may be placed in the associated .txt files... to fix this, please restart the script
