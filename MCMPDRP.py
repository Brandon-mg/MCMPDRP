from pypresence import Presence
import time
import requests
import json
#discord api id
appID = "" 
if appID=="":
    print("please add the required details")
    return
RPC = Presence(appID)
RPC.connect()
#server ip
ip=""
#server port
port="25565"
url="https://mcapi.us/server/status?ip="+ip+"&port="+port
#server online/offline message
richPresOnline = "Server is Online {}/{}"
richPresOffline = "Server is Offline"
while True:
    response = requests.get(url)
    serverStats = json.loads(response.text)
    online = serverStats["status"]
    maxPlayers = serverStats["players"]["max"]
    curPlayers = serverStats["players"]["now"]
    if(online=="success"):
        status=richPresOnline.format(curPlayers,maxPlayers)
    else:
        status=richPresOffline
    print(status)
    RPC.update(state=status)
    time.sleep(300)
