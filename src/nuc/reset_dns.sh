#!/bin/sh

ARSNOVA_ROUTER_USER="root"
ARSNOVA_ROUTER_HOST="192.168.1.1"

ssh "${ARSNOVA_ROUTER_USER}"@"${ARSNOVA_ROUTER_HOST}" killall -HUP dnsmasq