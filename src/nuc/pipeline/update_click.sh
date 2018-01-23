#!/bin/sh

BUILD_NO=$1
LINK=/home/arsnova/click-build

cd /home/arsnova/click-build-"$BUILD_NO"/build/bundle/programs/server
npm install
RESULT=$?

if [ "$RESULT" != "0" ]
then
	echo "Building new version of arsnova.click failed."
	exit 1
fi

sudo service arsnova-click stop
CURRENT_TARGET=$(readlink -f "$LINK")
rm "$LINK"
ln -s /home/arsnova/click-build-"$BUILD_NO" "$LINK"
sudo service arsnova-click start
rm -rf "$CURRENT_TARGET"
