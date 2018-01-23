#!/bin/sh

MY_IP=`hostname -I | awk '{print $1}'`

echo "${MY_IP}"
echo "${MY_IP} arsnova arsnova.eu arsnova.thm.de click.arsnova.eu voting.arsnova.eu cards.arsnova.eu" > arsnova.hosts
