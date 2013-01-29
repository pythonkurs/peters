#!/usr/bin/python

from peters import read_data
from peters import calc_status_repair 


doc = read_data()
iCounterRepair, iCounterAll = calc_status_repair(doc)
print str(iCounterRepair) + " out of " + str(iCounterAll) + " are under repair ("+ '%.1f' % (iCounterRepair/float(iCounterAll/100.0))  +"%)."
