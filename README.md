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
