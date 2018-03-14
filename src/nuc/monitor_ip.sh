#!/bin/sh

MY_IP=`cat last_ip.txt`

NEW_IP=`sh ip.sh`
if [ "$MY_IP" != "$NEW_IP" ]
then
    echo "[$(date)]: New IP detected: ${NEW_IP} (was: ${MY_IP})"
    echo "${NEW_IP}" > last_ip.txt
    sh detect.sh
    DETECT_STATUS=$?
    echo "[$(date)]: Router detection closed with status ${DETECT_STATUS}."
    if [ "0" = "${DETECT_STATUS}" ]
    then
	echo "[$(date)]: Connected to ARSnova-Router. Refreshing DNS..."
        sh send_hosts.sh
	SEND_STATUS=$?
	echo "[$(date)]: Updating DNS file closed with status ${SEND_STATUS}."
	sh reset_dns.sh
	RESET_STATUS=$?
	echo "[$(date)]: Reloading DNS closed with status ${RESET_STATUS}."
	echo "[$(date)]: DNS refresh finished."
    fi
fi
