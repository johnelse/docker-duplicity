#!/bin/bash

set -eux

. /tmp/duplicity/config/*

duplicity \
    /tmp/duplicity/backupdir \
    b2://${DUPLICITY_B2_ACCOUNT}:${DUPLICITY_B2_APPKEY}@${DUPLICITY_B2_BUCKET}
