import time, requests, json
loglistprevious=[]
filelocation=""#apache2 access.log file location
url = ""#discord webhook
api_key=""#open map quests api key
with open(filelocation,"r") as log:
    loglistprevious=log.readlines()
def running(loglistprevious):
    with open(filelocation,"r") as log:
        loglist=log.readlines()
    if loglist==loglistprevious or len(loglist)==0:
        return loglist
    else:
        try:
            int(loglist[len(loglist)-1][0])
            logline=str(loglist[len(loglist)-1]).split()
            ipaddress=logline[0]
        except:
            try:
                logline=str(loglist[len(loglist)-1]).split()
                ipaddress=logline[1]
            except:
                return
        try:
            resp=requests.get("http://extreme-ip-lookup.com/json/"+ipaddress)#Gets ip info
            jason=resp.json()
            try:
                urlmap="https://open.mapquestapi.com/staticmap/v4/getmap?key="+api_key+"desfi&size=600,400&zoom=9&center="+jason["lat"]+","+jason["lon"]#gets map
            except:
                urlmap=""
        except:
            jason={"org":"Unknown","city":"Unknown","country":"Unknown",}
            urlmap=""
        data={
            "embeds": [
            {
            "title": "JSite accessed",
            "description": "Site was accessed by ||"+ipaddress+"||",
            "url": "https://github.com/clearclarencs",
            "color": "705223",
            "image": {
                "url": urlmap
            },
            "fields": [
                {
                "name": ":office:",
                "value": jason["org"],
                "inline": "true"
                },
                {
                "name": ":cityscape:",
                "value": jason["city"],
                "inline": "true"
                },
                {
                "name": ":earth_africa:",
                "value": jason["country"],
                "inline": "true"
                }
            ]
            }
        ]
        }
        requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
        return loglist
while True:
    loglistprevious=running(loglistprevious)
    time.sleep(5)
