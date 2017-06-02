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
  * 

# Installation von ARSnova.click mit dem Installationsskript

## Raspbian
ARSnova.click kann mit dem Installationsskript voll automatisch installiert
werden. Dafür müssen die folgenden Schritte ausgeführt werden.
  * `sudo apt-get update`
  * `sudo apt-get insall git`
  * `git clone https://git.thm.de/arsnova/arsnova-router.git`
  * `cd arsnova-router`
  * `./install_raspbian_jessie`

## Ubuntu 16.04.02
Bei der Installation muss das Skript `install_ubuntu_16.04.2` ausgeführt werden.
Dafür muss das Repository geklont werden.
  * `sudo apt-get update`
  * `sudo apt-get install git`
  * `git clone https://git.thm.de/arsnova/arsnova-router.git`
  * `cd arsnova-router`
  * `./install_ubuntu_16.04.2`
