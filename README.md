
So i hear the UK government wants to make a porn filter. About bloody time i reckon. I'm fed up of happily browsing the Internet for boobs, only to have non-porn related subject matter thrust down my face hole.

So taking inspiration from other great Internet filtering nations such as [North Korea, China, Syria, Iran, Cuba, Bahrain, Belarus, Burma, Uzbekistan, Saudia Arabia and Vietnam](http://en.wikipedia.org/wiki/Internet_censorship_by_country) I decided to help out the UK government and build an Internet filter that only allows pornographic material through. 

You're Welcome.


Setting Up
==========
All code is available here [https://github.com/SickSad/UKPR0nFilter](https://github.com/SickSad/UKPR0nFilter)

Just follow this simple step-by-step video walk-through and you'll have a porn filter running in no time!
[http://www.youtube.com/watch?v=xJfyNwM6Lw8](http://www.youtube.com/watch?v=xJfyNwM6Lw8)

Nerd Stuff
==========

The filter is a dns server which checks all queries against the [OpenDNS](http://www.opendns.com/home-solutions/parental-controls/) FamilySheild DNS server. Any request that is denied by OpenDNS is then allowed by our DNS server, and any request allowed by OpenDNS is blocked by us.

The server itself it built using the [python Twisted framework](http://twistedmatrix.com/) which handles both the DNS requests and acts as a simple web-server to host the denial page.