Title: System Design Primer: Reverse Proxy
Date: 2019-01-16
Status: draft
Summary: Reverse proxies, comparison between load balancers
CoverImage: http://i.imgur.com/6SbxQah.png
Thumbnail: http://i.imgur.com/oCWLuMC.png

## Reverse proxy (web server)

<p align="center">
  <img src="http://i.imgur.com/n41Azff.png">
  <br/>
  <i><a href=https://upload.wikimedia.org/wikipedia/commons/6/67/Reverse_proxy_h2g2bob.svg>Source: Wikipedia</a></i>
  <br/>
</p>

A reverse proxy is a web server that centralizes internal services and provides unified interfaces to the public.  Requests from clients are forwarded to a server that can fulfill it before the reverse proxy returns the server's response to the client.
