#!/bin/sh
# Simple script to detect if we are connected to the ARSnova Router.

ARS_ROUTER_HOST="192.168.1.1"
ARS_ROUTER_PATH="/cgi-bin/luci"
ARS_ID_STRING="ARSnova-Router"

# Download the configuration UI and check if there is any mention of our Router
curl -s http://"${ARS_ROUTER_HOST}""${ARS_ROUTER_PATH}" | grep "${ARS_ID_STRING}" > /dev/null
