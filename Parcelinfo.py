#!/usr/bin/python

import sys, urllib, json


parcellist = raw_input("Enter comma sepreated list of parcel: ").split(',')
#"""
print "************************************************************************"
for parcel in parcellist:
        url = 'https://parcelv1.api.spsprod.in/rest/parcels/%s'%parcel
        op = urllib.urlopen(url).read()
        jdata = json.loads(op)
        print "ChildParceluid = ",jdata['legacyParcelUid']
        print "ParentParceluid = ",jdata['legacyParentParcelUid']
        print "ChildParcelServiceName = ",jdata['service']['name']
        print "ChildParcelstatus = ",jdata['status']['status']
        print "************************************************************************"
#"""
#print parcellist

