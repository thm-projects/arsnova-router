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

# Hardwareaufbau
Als Hardware kann ein Raspberry Pi oder ein handelsüblicher Rechner verwendet
werden. Dabei muss nur der Aufbau der Hardware beachtet werden. Wichtig ist,
dass bei der Installation eine Internetverbindung besteht, da Packete aus dem
Packetmanager installiert werden.

Bei normalem Betrieb nach der Installation wird keine Internetverbindung
benötigt. Es muss ein geeigneter Router/Access Point verwendet und mit
dem Rechner verbunden werden. Dann können Benutzer auf das ARSnova.click zugreifen und
verwenden.

# Installieren des Systems
## Raspbian
  * Image `<Datum>-raspbian-<Version>.img` herunterladen
  * Mit `sudo dd if=/dev/sdX of=<Pfad>/<Datum>-raspbian-<Version>.img` auf die
    SD-Karte kopieren
  * Das erste Laufwerk muss eingehängt werden mit `sudo mount /dev/sdX1
    <Mountpunkt>`
  * Es muss die Datei **ssh** angelegt werden mit `sudo touch <Mountpunkt>/ssh`.
    Diese Datei ist wichtig, da sonst kein SSH Zugriff auf das Raspberry Pi
    besteht.
  * Nach dem schreiben der Datei kann die SD-Karte ausgehängt werden mit
    `sudo umount <Mountpunkt>`.
    Die SD-Karte kann jetzt mit dem Raspberry Pi verwendet werden.

## Ubuntu 16.04.02
Bei der installation muss sicher gestellt werden, dass der Benutzer
`arsnova` angelegt wird und der Name des Rechners muss ebenfalls `arsnova`
lauten.
  * Für die Installaion siehe offizielle [Ubuntu Anleitung](https://www.ubuntu.com/download/desktop/install-ubuntu-desktop).

## Elementary OS 0.4.1 Loki
Bei der installation muss sicher gestellt werden, dass der Benutzer
`arsnova` angelegt wird und der Name des Rechners muss ebenfalls `arsnova`
lauten.
  * Für die Installaion siehe offizielle [Elementary OS Anleitung](https://elementary.io/docs/installation#creating-an-installation-medium).

# Installation von ARSnova.click mit dem Installationsskript
Bei der Installation muss sichergestellt werden, dass eine Internetverbindung
besteht. Während der Installation werden Packete aus dem Internet geladen und
installiert.

Bevor eine Installation starten kann, muss `git` installiert werden. Das kann mit
dem Packetmanager der gewählten Linuxdistribution gemacht werden. Bei Debian
bassierten Distributionen wird `apt-get` verwendet. In der Regel müssen die
Packetquellen aktualisiert werden, bevor eine Packet installiert werden kann.
  * `sudo apt-get update`
  * `sudo apt-get install git`

Nachdem git installiert ist, kann das ARSnova.click Repository geklont werden.
  * `git clone https://git.thm.de/arsnova/arsnova-router.git`

Als letztes muss in das Verzeichniss von **arsnova-router** gewechselt werden.
  * `cd arsnova-router`

## Raspbian
ARSnova.click kann mit dem Installationsskript voll automatisch installiert
werden. Dafür müssen die folgenden Schritte ausgeführt werden.
  * `./install_raspbian_jessie`

## Elementary OS 0.4.1 Loki
ARSnova.click kann mit dem Installationsskript voll automatisch installiert
werden. Dafür müssen die folgenden Schritte ausgeführt werden.
  * `./install_elementary_os_0.4.1_loki`

## Ubuntu 16.04.02
ARSnova.click kann mit dem Installationsskript voll automatisch installiert
werden. Dafür müssen die folgenden Schritte ausgeführt werden.
  * `./install_ubuntu_16.04.2`

# Alpha Bundle

The "Alpha Bundle" is our first working prototype of ARSnova Router consisting of a Linksys WRT3200ACM (the *Router*) and an Intel NUC i7 (the *Server*).

## Linksys WRT3200ACM

We summarize the key settings:

### Connectivity Tab

- DHCP needs to be enabled with the IP range above 42, preferrably starting at 100.
- As static DNS server, the *Server*'s IP needs to be put in

### Security Tab

- Enable simple port forwarding for port 53 (DNS) to the *Server*'s IP. This is required because otherwise, domain name resolution does not work reliably.

## Intel NUC i7

### DNS

The NUC has a fixed IP address: `192.168.1.42`. This address is associated with the domains:

* `arsnova.click.local`
* `arsnova.voting.local`
* `arsnova.local`
* `arsnova`

To set up the static IP, edit `/etc/network/interfaces`:

> auto eno1
> iface eno1 inet static
> address 192.168.1.42
> netmask 255.255.255.0
> gateway 192.168.1.1

`eno1` is the network interface (ethernet).

Then, edit `/etc/hosts` to set up the domains:
> 192.168.1.42    arsnova.click.local arsnova.voting.local arsnova.local arsnova

Next, install and configure the DNS server:

```
$ sudo apt-get install -y dnsmasq
```

Edit /etc/dnsmasq.conf:
> listen-address=127.0.0.1
> listen-address=192.168.1.42

```
$ sudo service dnsmasq restart
```

Note that these settings have not been tested in the presence of a working Internet connection.

### SSH

It suffices to install OpenSSH to enable SSH access:

```
$ sudo apt-get install -y openssh-server
```

# TODO
- [X] Install DNS server
- [X] Install SSH server
- [ ] Install mDNS server (required to fix `.local` domains on Android and Linux)
- [ ] Enable HTTPS for arsnova.click.local
- [ ] Write configuration scripts based on this README (eg. for Puppet)

## Old TODOs (may be deleted)
-  Bei der Raspbian installation gibt es das Problem, dass die Konfiguration von MongoDB nicht direkt ausgeführt werden kann. Es muss ca. 1 Minute gewartet werden, bevor die Datenbank konfiguriert werden kann. Die Ursache für dieses Problem ist nicht wirklich klar. Ein erarbeiteter Workaround ist die Konfigurationsanweisung `mongo < mongo_config_v2.4.10.js` deutlich nach dem starten der Datenbank zu verschieben. In der Datei `install_rasbian_jessie` wurde diese Anweisung vor das Systemupdate verschoben.
