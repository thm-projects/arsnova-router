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

- [ ] Explain overall idea: users connect to Router through Wifi, redirects requests to NUC.
 
## Linksys WRT3200ACM

- [ ] OpenWRT installation, details https://openwrt.org/toh/linksys/linksys_wrt3200acm
- [ ] List of enabled services (SSH, dnsmasq)
- [ ] Wifi settings
- [ ] Wiring of Router and Server using a LAN cable

## Intel NUC i7

- [ ] Mouse, Keyboard, HDMI cable
- [ ] ARSnova Voting installation follows official documentation

### DNS

- [ ] IP change detection script
- [ ] DNS update script

### SSH

For development purposes, it will make sense to have SSH access. It suffices to install OpenSSH to enable SSH:

```
$ sudo apt-get install -y openssh-server
```
