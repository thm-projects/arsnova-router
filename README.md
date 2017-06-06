# Hardwareaufbau
Als Hardware kann ein Raspberry Pi oder ein handelsüblicher Rechner verwendet
werden. Dabei muss nur der Aufbau der Hardware beachtet werden. Wichtig ist,
dass bei der Installation eine Internetverbindung besteht, da Packete aus dem
Packetmanager installiert werden.

Bei normalen Betrieb nach der Installation wird keine Internetverbindung
benötigt. Es muss ein geeigneter Router/Access Point verwendet werden und mit
dem Rechner verbunden. Dann können Benutzer auf das ARSnova.click zugreifen und
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
lautet.
  * Für die Installaion siehe offizielle [Ubuntu Anleitung](https://www.ubuntu.com/download/desktop/install-ubuntu-desktop).

## Elementary OS 0.4.1 Loki
Bei der installation muss sicher gestellt werden, dass der Benutzer
`arsnova` angelegt wird und der Name des Rechners muss ebenfalls `arsnova`
lautet.
  * Für die Installaion siehe offizielle [Elementary OS Anleitung](https://elementary.io/docs/installation#creating-an-installation-medium).

# Installation von ARSnova.click mit dem Installationsskript
Bei der Installation muss sichergestellt werden, dass eine Internetverbindung
besteht. Während der Installation werden Packete aus dem Internet geladen und
installiert.

Bevor eine Installation starten kann muss `git` installiert werden. Das kann mit
dem Packetmanager der gewählten Linuxdistribution gemacht werden. Bei Debian
bassierten Distributionen wird `apt-get` verwendet. In der Regel müssen die
Packetquellen aktualisiert werden bevor eine Packet installiert werden kann.
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

