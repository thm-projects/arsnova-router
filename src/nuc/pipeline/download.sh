#!/bin/sh

get_build_no()
{
	BUILD_NO=`curl --head --silent $1 | grep "Location" | tr -dc '0-9'`
	if [ "$BUILD_NO" -eq "$BUILD_NO" ] 2>/dev/null; then
		return "$BUILD_NO"
	fi
	
	echo "Could not get current build number. Exiting."
	exit 1
}

download_build()
{
	echo "$1" > "$3".build
	wget "$2" -O "$3"-"$1".zip
	unzip -q "$3"-"$1".zip -d /home/arsnova/"$3"-build-"$1"
	rm "$3"-"$1".zip
}

