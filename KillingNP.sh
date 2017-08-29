#!/bin/bash

PARTNER=$1
## Featching the instance from Marathon
ID=$(curl -s -u 'mesos:6EMa3BlDXlFd' https://prod-mesos.spsprod.in/marathon/v2/apps/netsuite-router-prod-3.5.5.4\/$PARTNER | python -c 'import sys,json; print json.load(sys.stdin)["app"]["tasks"][0]["id"]')
## Displaying the patner name & instance ID
echo -e "Killing $1/$ID"
## Killing the releated patner instance 
curl -s -u 'mesos:6EMa3BlDXlFd' -X DELETE https://prod-mesos.spsprod.in/marathon/v2/apps/netsuite-router-prod-3.5.5.4\/$PARTNER\/tasks\/$ID

## FYI: While killing the instance just give the scriptname.sh (Patner name)
