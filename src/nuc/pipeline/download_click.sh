#!/bin/sh

CLICK_PIPE="https://git.thm.de/arsnova/arsnova.click/-/jobs/artifacts/staging/download?job=build"

. "./download.sh"

get_build_no $CLICK_PIPE
CLICK_BUILD_NO=$?

LAST_CLICK_BUILD=`cat click.build`

if [ "$LAST_CLICK_BUILD" != "$CLICK_BUILD_NO" ]
then
	download_build $CLICK_BUILD_NO $CLICK_PIPE "click"
	sh update_click.sh $CLICK_BUILD_NO
else
	exit 42
fi

