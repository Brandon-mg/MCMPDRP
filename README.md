# MCMPDRP
This is a simple python script that allows you to show your chosen servers status on your discord profile.

## Requires
Python 3.8+

Requests

[PyPresence](https://github.com/qwertyquerty/pypresence)

## Working
This script simply requests the status of a server using [mcapi.us](https://mcapi.us/), then parses the json to get the server status and player count.

Json example can be found on the mcapi site.

Currently only checks if the server is running and player count every 5 minutes. Mcapi caches query results for five minutes anyways so reducing the timer will do nothing.

## Instructions

Follow PyPresence instructions to get your App ID

edit the variables to add the App ID, server IP, and the server port.

run the program, discord will change the profile activity, if theres no activity attach a program by adding it to discords activity settings.
