#!/bin/sh

COPY=$(aws s3 cp $1 /tmp/copy.txt)
LINE=$((AWS_BATCH_JOB_ARRAY_INDEX + 1))
echo $LINE
LINE=$(sed -n ${LINE}p /tmp/copy.txt)
echo $LINE
VAR=( $LINE )
SOURCEKEY=${VAR[0]}
DESTINATIONKEY=${VAR[1]}
SOURCEBUCKET=${VAR[2]}
DESTINATIONBUCKET=${VAR[3]}
echo $(python ./CopyToS3-master/transferserver.py $SOURCEKEY $DESTINATIONKEY $SOURCEBUCKET $DESTINATIONBUCKET)
