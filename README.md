# ARSnova Router

ARSnova Router delivers the ARSnova experience into classrooms that either have poor or no internet connection at all.

With ARSnova Router, you "Bring Your Own Network" (BYON), with a local Wifi just for you and your students. You access ARSnova without outside interference for a fast, reliable, and secure experience.

Please see our white paper for further details (currently german only):

["Strategien für die Bereitstellung eines skalierbaren Audience-Response-Systems: Vom ARS-Router bis zum Cloud-Deployment"](https://git.thm.de/arsnova/arsnova-router/raw/master/arsnova-delfi-paper-THM.pdf)

-----------

:construction: This README is currently under construction. :construction:

-----------

ARSnova Router consists of two parts: a Wifi "Router" to create the wireless infrastructure, and a "Server" hosting a local ARSnova installation. Throughout this README, we will refer to "Router" and "Server" to mean the Wifi router and the computer, respectively.

This repository is for the technical setup of both the Wifi "Router" and the ARSnova "Server."

# Alpha Bundle

The "Alpha Bundle" is our first working prototype of ARSnova Router consisting of a Linksys WRT3200ACM (the *Router*) and an Intel NUC i7 (the *Server*).

- [ ] Explain overall (technical) idea: users connect to Router through Wifi, redirects requests to NUC. NUC detects presence of Router, applies changes to the Router's DNS entries.

## Usage scenarios

The following usage scenarios are possible with the Alpha Bundle: Headless, and using a video projector.

### Headless

The NUC can work "headless", ie. without connecting it to a monitor or a video projector in the classroom. This is useful if ARSnova should be controlled from a separate machine such as a laptop, for example, to show a slide presentation and to switch back and forth between the presentation and ARSnova.

For this setup, Router and Server need to be wired up exactly as explained above, but no further steps are necessary. The separate laptop connects to the ARSnova wifi like all other users.

### Using a video projector

It is also possible to directly present from the NUC by connecting it with a HDMI cable to the video projector. A mouse and keyboard are then necessary to control the browser.

## Linksys WRT3200ACM

- [ ] OpenWRT installation, details https://openwrt.org/toh/linksys/linksys_wrt3200acm
- [ ] List of enabled services (DHCP, SSH, dnsmasq)
- [ ] Wifi settings
- [ ] Wiring of Router and Server using a LAN cable

## Intel NUC i7

ARSnova Voting is installed directly on the NUC following the official documentation. This means that the NUC contains an Apache CouchDB and runs Apache Tomcat to serve both ARSnova's backend and its mobile client.

Voting is availabe at `voting.arsnova.eu`.

### DNS

The NUC should be usable as a regular desktop PC if not connected to the Router. This prohibits the usage of a static IP adress, even though this would make it a lot easier to work with the Router. This is because the network interface would need to be reset to DHCP in cases of regular Internet usage.

When set to DHCP, however, the Router could change the Server's IP adress at any time.

- [ ] IP change detection script
- [ ] DNS update script

## Technical issues

- [ ] Usage of HTTPS/WSS
- [ ] Search bars of modern browsers discourage usage of short domains like "arsnova"
- [ ] 
