#!/usr/bin/python
import os
import commands
import json


## Here giving access key's for Sumo and featching catche info
SLCURL="curl -b /tmp/slcookie.txt -c /tmp/slcookie.txt -s"
AID='suDZof0If12GLA'
AKEY='gOkBA5zEQ2Ly2mgUtFCBHutOCGmXxeXzIfRvOwZ6EzVyQ6XOWttlFgeALwt7m2JX'

#U = 'rperla@spscommerce.com'

## Here is the search query from sumo and featching only from last 30 minutes
Q = "_index%3Ddc4_fi4_logs%20_sourceCategory%3Dapp_dc4_fi4*%20AND" + "%22java.lang.OutOfMemoryError%3A%22"
R = '''%s -u %s:%s "https://api.us2.sumologic.com/api/v1/logs/search?q=%s&from=$(TZ='America/Chicago' date -Iseconds --date='30 minutes ago')"'''%(SLCURL,AID,AKEY,Q)

OP = commands.getoutput(R)
print OP

