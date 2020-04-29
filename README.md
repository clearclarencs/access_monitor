# Site access monitor
Discord site access monitor for apache2

Run on website server and each time a client accesses you site it is added to access.log which this script monitors and whan it changes send a discord wehook of the ip and information about the ip address.

![Example of webhook](https://cdn.discordapp.com/attachments/703941655992205342/705130289009131711/unknown.png)

Uses https://extreme-ip-lookup.com/ api for ip location, does not require api key.

Uses https://developer.mapquest.com/ api for image of location, requires api key.
