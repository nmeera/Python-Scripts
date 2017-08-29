#!/usr/bin/python

import os
import commands

qfbprime01 = "clear; echo Connecting to qfbprime01.....; echo; echo ---------qfbprime01---------; curl -s http://qfbprime01.mps.spscommerce.net:8000 | grep ^FILEBROKER_WORK_ | sed -e 's/<br>//g'; echo"

catalog = "echo Connecting to catalog-queue.us-east-1.....; echo; echo ---------catalog-queue.us-east-1---------; curl -s http://catalog-queue.us-east-1.spsprod.in:8000 | grep ITEM_VALIDATION_CURRENT | sed -e 's/<br>//g'; echo"


qdc4prime01 = "echo Connecting to qdc4prime01.....; echo;  echo ---------qdc4prime01---------; curl -s http://qdc4prime01.mps.spscommerce.net:8000 | grep ^XG_ | sed -e 's/<br>//g'; echo"

preqfiprime01 = "echo Connecting to preqfiprime01.....; echo; echo ---------preqfiprime01---------; curl -s http://preqfiprime01.us-east-1.spspreprod.in:8000 | grep xg | grep -E 'large|small' | sed -e 's/<br>//g'; echo"

qwebprime = "echo Connecting to qebprime01........; echo; echo ---------qwebprime---------;curl -s http://qwebprime01.mps.spscommerce.net:8000 | grep WEBFORMS_ | sed -e 's/<br>//g'; echo"

qfiprime01 = "echo Connecting to qfiprime01.....; echo; echo ---------qfiprime01---------; curl -s http://qfiprime01.us-east-1.spsprod.in:8000 | grep xg | grep -E 'large|small' | sed -e 's/<br>//g'; echo"

AS2Cluster1 = "echo Connecting to AS2Cluster1.....; echo; echo ---------as2app11---------; curl -s http://as2app11.mps.spscommerce.net:8000 | grep B2BEventQueue_CURRENT | sed -e 's/<br>//g'; echo"

AS2Cluster2 = "echo Connecting to AS2Cluster2.....; echo; echo ---------as2app21---------; curl -s http://as2app21.mps.spscommerce.net:8000 | grep B2BEventQueue_CURRENT | sed -e 's/<br>//g'; echo"

AS2Cluster3 = "echo Connecting to AS2Cluster3.....; echo; echo ---------as2app31---------; curl -s http://as2app31.us-east-1.spsprod.in:8000 | grep dist_B2BEventQueue_auto_CURRENT | sed -e 's/<br>//g'; echo"

B2B = "echo Connecting to B2B.....; echo; echo -------B2B---------; curl -s http://dc4b2b01.mps.spscommerce.net:8000 | grep B2B |grep -E 'B2B_OUT_QUEUE_CURRENT|B2B_IN_QUEUE_CURRENT|B2BEventQueue_CURRENT|B2BListeningQueue_CURRENT' | sed -e 's/<br>//g'; echo"

QFB = commands.getoutput(qfbprime01)
QCAT = commands.getoutput(catalog)
#QEH = commands.getoutput(EHQueue)
QDC4 = commands.getoutput(qdc4prime01)
PREQFI = commands.getoutput(preqfiprime01)
QWEB = commands.getoutput(qwebprime)
QFI = commands.getoutput(qfiprime01)
AS1 = commands.getoutput(AS2Cluster1)
AS2 = commands.getoutput(AS2Cluster2)
AS3 = commands.getoutput(AS2Cluster3)
B2B4 = commands.getoutput(B2B)

print QFB, QCAT, QDC4, PREQFI, QWEB, QFI, AS1, AS2, AS3, B2B4

