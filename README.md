# Manuelle Einrichtung eines Raspberry Pi mit ARSnova.click
Hier wird erklärt wie ein Raspberry Pi mit ARSnova.click eingerichtet wird.
Dabei wird Schritt für Schritt gezeigt was nötig ist für die Einrichtung.

1. Aktuelles **Raspbian** herunterladen und auf SD-Larte aufspielen.

2. Zuerst sollte das Raspberry Pi auf den aktuellsten Stand gebracht werden mit:

   `sudo apt-get update`

   `sudo apt-get install dnsmasq`

   `sudo apt-get upgrade`

   Ein Neustart des Systems ist erforderlich, wenn ein Kernelupdate
   durchgeführt wurde mit `sudo reboot`.

3. Als nächstes muss NodeJS installiert und eingerichtet werden.
   Um die aktuellste Verison von NodeJS zu erhalten, muss das offizielle
   Repository eingefügt werden.

   `curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -`

   `sudo apt-get update`

   Nachdem das Repository erfolgreich eingefügt wurde, muss NodeJS installiert
   werden.

   `sudo apt-get install nodejs`

   Jetzt müssen alle nötigen Erweiterungen NodeJS-Erweiterung installiert
   werden.

   `npm install forever fibers underscore source-map-support semver -g`

4. Um ARSnova.click zu nutzen muss noch MongoDB installiert werden und kann von
   dem standard Debian-Repository installiert werden.

   `sudo apt-get install mongodb'

   Jetzt muss MongoDB gestartet werden.

   `systemctl enable mongodb.service`

   `systemctl start mongodb.service`

    Es ist nötig die Datenbank einzurichten bevor der nächste Schritt
    durchgeführt werden. Dafür muss man zuerst das Kommando `mongo` ausgeführt
    werden und damit wird man in die MongoDB-Shell wechseln. In der
    MongoDB-Shell folgende Kommandos ausgeführt werden.

    `use arsnova_click`

    `db.addUser({user:"meteor", pwd:"meteor", roles:["readWrite"]})`

    `exit`

    Wenn die Tabelle *arsnova_click* angelegt wurde, muss die MongoDB
    neugestartet werden.

    `systemctl restart mongodb.service`

5. Als letztes muss Nginx installiert werden. Es muss mindestens die Version
   1.10 installiert werden, da mit älteren Versionen wurde ARSnova.click nicht
   getestet.
   Im Repository von Rasbian, mit dem Image **2017-04-10-raspbian-jessie.img**,
   ist nur die Version 1.6.2 zu finden. Um einen neuere Version zu installieren
   müssen die Backports verwendet werden. Dazu muss die die Datei
   `/etc/opt/sources.list.d/backports.list` angelegt werden und folgendes in die
   Datei geschrieben werden.

   `deb http://ftp.debian.org/debian jessie-backports main`

   Jetzt muss dieses neue Repository apt bekannt gemacht werden.

   `sudo apt-get update`

   Es kann dazu kommen, dass bestimmte public keys fehlen. Wenn das nicht
   zutrifft dann kann der nächste Schritt übersprungen werden.

   `gpg --keyserver pgpkeys.mit.edu --recv-key  <public key>`

   `gpg -a --export <public key> | sudo apt-key add -`

   `sudo apt-get update`

   Nach dem aktualisieren der Packetquellen kann das NodeJS-Packet installiert
   werden.

   `sudo apt-get -t jessie-backports install nginx-full`

   Als nächstes muss Nginx konfiguriert werden. Dazu muss die
   Konfigurationsdatei

   `wget https://git.thm.de/arsnova/arsnova.click/raw/server-config/config/app-server/etc/nginx/sites-available/meteor`

   `sudo mv meteor /etc/nginx/sites-available`

   `ln -s /etc/nginx/sites-enabled/meteor  /etc/nginx/sites-available/meteor`

   `sudo rm  /etc/nginx/sites-enabled/default`

6. Als letztes muss ARSnova.click vom Repository heruntergeladen werden.

   `wget https://git.thm.de/arsnova/arsnova.click/builds/artifacts/master/download?job=build -O artifacts.zip`

   `unzip artifacts.zip`

   Nach dem entpacken von ARSnova.click muss die Konfigurations heruntergeladen
   werden. Diese wird später im systemd Startskript benötigt.

   `wget https://git.thm.de/arsnova/arsnova.click/raw/staging/arsnova.click/settings.json`

