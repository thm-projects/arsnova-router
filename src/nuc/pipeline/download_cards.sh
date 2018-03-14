#!/bin/sh

CARDS_PIPE="https://git.thm.de/arsnova/flashcards/-/jobs/artifacts/staging/download?job=build"

. "download.sh"

get_build_no $CARDS_PIPE
CARDS_BUILD_NO=$?

LAST_CARDS_BUILD=`cat cards.build`

if [ "$LAST_CARDS_BUILD" != "$CARDS_BUILD_NO" ]
then
	#download_build $CARDS_BUILD_NO $CARDS_PIPE "cards"
	#sh update_cards.sh $CARDS_BUILD_NO
	echo "Updating cards: TODO!"
else
	exit 42
fi

