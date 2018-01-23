#!/bin/sh

ARS_ROUTER_USER="root"
ARS_ROUTER_HOST="192.168.1.1"

scp arsnova.hosts "${ARS_ROUTER_USER}"@"${ARS_ROUTER_HOST}":/tmp/hosts
