# Paper zum Projekt

["Strategien für die Bereitstellung eines skalierbaren Audience-Response-Systems: Vom ARS-Router bis zum Cloud-Deployment"](https://git.thm.de/arsnova/arsnova-router/raw/master/arsnova-delfi-paper-THM.pdf)

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

## Ubuntu 16.04.02
ARSnova.click kann mit dem Installationsskript voll automatisch installiert
werden. Dafür müssen die folgenden Schritte ausgeführt werden.
  * `./install_ubuntu_16.04.2`

## Elementary OS 0.4.1 Loki
ARSnova.click kann mit dem Installationsskript voll automatisch installiert
werden. Dafür müssen die folgenden Schritte ausgeführt werden.
  * `./install_elementary_os_0.4.1_loki`

# TODO
  * DNS installieren und einrichten.
  * Statische IP Adresse anlegen in dhcpcd.conf, das funktioniert zur Zeit nur
    bei Raspbian.
    Das wird für dnsmasq benötigt.
  * Bei der Raspbian installation gibt es das Problem, dass die Konfiguration
    von MongoDB nicht direkt ausgeführt werden kann. Es muss ca. 1 Minute
    gewartet werden, bevor die Datenbank konfiguriert werden kann. Die Ursache
    für dieses Problem ist nicht wirklich klar. Ein erarbeiteter Workaround ist
    die Konfigurationsanweisung `mongo < mongo_config_v2.4.10.js` deutlich
    nach dem starten der Datenbank zu verschieben. In der Datei
    `install_rasbian_jessie` wurde diese Anweisung vor das Systemupdate
    verschoben.

