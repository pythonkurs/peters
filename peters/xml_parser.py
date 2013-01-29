#!/usr/bin/python


import untangle
import urllib2

def read_data():
	xml_url = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"


	feed = urllib2.urlopen(xml_url)

	doc = untangle.parse(feed.read())

	return doc

def calc_status_repair(doc):
	outages = doc.NYCOutages.outage

	iCounterRepair = 0
	iCounterAll = 0

	for entry in outages:
		outage = entry.reason.cdata
		if outage == "REPAIR":
			iCounterRepair += 1
		iCounterAll += 1
	return iCounterRepair, iCounterAll

doc = read_data()
iCounterRepair, iCounterAll = calc_status_repair(doc)
print str(iCounterRepair) + " out of " + str(iCounterAll) + " are under repair ("+ '%.1f' % (iCounterRepair/float(iCounterAll/100.0))  +"%)."