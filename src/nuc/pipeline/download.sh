#!/bin/sh

CLICK_PIPE="https://git.thm.de/arsnova/arsnova.click/-/jobs/artifacts/staging/download?job=build"
CARDS_PIPE="https://git.thm.de/arsnova/flashcards/-/jobs/artifacts/staging/download?job=build"

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

get_build_no $CLICK_PIPE
CLICK_BUILD_NO=$?
get_build_no $CARDS_PIPE
CARDS_BUILD_NO=$?

LAST_CLICK_BUILD=`cat click.build`
LAST_CARDS_BUILD=`cat cards.build`

if [ "$LAST_CLICK_BUILD" != "$CLICK_BUILD_NO" ]
then
	download_build $CLICK_BUILD_NO $CLICK_PIPE "click"
	sh update_click.sh $CLICK_BUILD_NO
fi

if [ "$LAST_CARDS_BUILD" != "$CARDS_BUILD_NO" ]
then
	#download_build $CARDS_BUILD_NO $CARDS_PIPE "cards"
	#sh update_cards.sh $CARDS_BUILD_NO
	echo "Updating cards: TODO!"
fi

