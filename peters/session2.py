def read_data():
	import untangle
        import urllib2
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
