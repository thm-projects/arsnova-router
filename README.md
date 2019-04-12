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

The NUC should be usable as a regular desktop PC if not connected to the Router. This prohibits the usage of a static IP address, even though this would make it a lot easier to work with the Router. This is because the network interface would need to be reset to DHCP in cases of regular Internet usage.

When set to DHCP, however, the Router could change the Server's IP address at any time. This would mean that the domain records need to be changed accordingly.

The Server, therefore, monitors its own IP address and whenever a change is detected, and the Server is connected to the Router, a DNS change is initiated. This is implemented with a cron job that periodically invokes a script ([src/nuc/monitor_ip.sh](src/nuc/monitor_ip.sh)) to check for an IP address change.

The script uploads a new DNS host file to the Router, so that the DNS entries are updated to the new IP address. The Router has a specific directory for this, which by default is configured to be at `/tmp/hosts`. We then send `dnsmasq` (the tool we use for DNS) the `HUP` signal, which forces it to re-read all host files. The advantage of this approach is that we do not need to restart DNS whenever we change the host files.

## Technical issues

### Usage of HTTPS/WSS

Since we have a local network, we are unable to provide an official SSL certificate. Self-signed certificates are not an option anymore, because modern browsers display huge warning messages which kill usability and user experience.

A possible solution would be to request an official certificate for the fake domains we use in the local network and then to install them on the Server. While this could work for the case of our single Alpha Bundle, a couple of issues arise in this scenario:

1. Free certificates like "let's encrypt" are only valid for short periods of time. An update process would be necessary to renew the certificates in time, which would mean the NUC must be connected to the Internet before the certificate expires.
2. Installing the certificates on the Server means to give up control. Effectively, the certificate is passed to a third-party. This is against the TOS of most certificate providers, including "let's encrypt." To counter this problem, the third-party would need to request their own certificates for the ARSnova domains.
3. Every new Bundle would need its own certificate, so new subdomains are needed. Thinking about scale, these domain names will probably get increasingly user-unfriendly the more Bundles are produced.

### On domain names

It would be best to use short domain names like "arsnova". However, modern browsers have a search bar instead of an URL bar, which will interpret "arsnova" as a search term, not as a domain name. Only if the name is extended to, eg., "arsnova.eu", will it be correctly parsed and auto-completed to a URL.

Using TLDs like "arsnova.eu" ties back to the problems of the previous section: If a user has ever visited "arsnova.eu" before, the certificate is stored in the browser. Any other certificate (or even a missing certificate) will cause the browser to display warnings. The domain name for the Bundle would thus have to be "fresh."

# Credits

ARSnova is powered by Technische Hochschule Mittelhessen - University of Applied Sciences.
