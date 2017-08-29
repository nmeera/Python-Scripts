import os
import commands
import json
#import jsonpointer

Capability = list()

SLCURL="curl -b /tmp/slcookie.txt -c /tmp/slcookie.txt -s"
AID='suDZof0If12GLA'
AKEY='gOkBA5zEQ2Ly2mgUtFCBHutOCGmXxeXzIfRvOwZ6EzVyQ6XOWttlFgeALwt7m2JX'

#Cap = raw_input('Enter comma separated capabilities list: ')
#inputList = os.environ["CapabilityUID"]
#Capability = inputList.split(',')

## It will check from last 10 minutes capabilities which are actively  running on sumologic
Q = "_sourceCategory%3D%20app_fb_prod_worker*%20%7C%20parse%20%22%5C%22CapabilityUid%5C%22%3A%5C%22*%5C%22%22%20as%20CapUID%20%7C%20formatDate(now()%2C%20%22yyyy-MM-dd%20HH%3Amm%3AssZZZZ%22)%20as%20today%20%7Ccount_frequent%20today%2C%20capuid%20%7C%20sort%20by%20today%20"
R = '''%s -u %s:%s "https://api.us2.sumologic.com/api/v1/logs/search?q=%s&from=$(TZ='America/Chicago' date -Iseconds --date='10 minutes ago')"'''%(SLCURL,AID,AKEY,Q)
OP = commands.getoutput(R)

print OP

