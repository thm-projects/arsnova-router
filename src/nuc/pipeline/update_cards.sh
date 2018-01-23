#!/bin/sh

BUILD_NO=$1
LINK=/home/arsnova/cards-build

cd /home/arsnova/cards-build-"$BUILD_NO"/build/bundle/programs/server
npm install
RESULT=$?

if [ "$RESULT" != "0" ]
then
	echo "Building new version of arsnova.click failed."
	exit 1
fi

sudo service arsnova-cards stop
CURRENT_TARGET=$(readlink -f "$LINK")
rm "$LINK"
ln -s /home/arsnova/cards-build-"$BUILD_NO" "$LINK"
sudo service arsnova-cards start
rm -rf "$CURRENT_TARGET"
