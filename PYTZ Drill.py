##Python:         3.6.1
##
##Author:         David Jackson
##                jaxdavio@yahoo.com
##
##Purpose:        To show from Portland, OR, Headquarters, the time(zone) of both New York
##                & London branches, and if they are open or closed with local 9am-9pm hours.
##


from datetime import datetime
from pytz import timezone    
import time

portland = timezone('America/Los_Angeles')
hq_time = datetime.now(portland)
time.sleep(1)
print ('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print (hq_time.strftime('Portland, OR, Headquarters Date & Time:' '\n'
                        '%m-%d-%Y %H:%M:%S'))
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
time.sleep(3)

new_york = timezone('America/New_York')
ny_time = datetime.now(new_york)
new_yorkBranch = int(ny_time.strftime('%H%M%S'))

if new_yorkBranch >= 9 and new_yorkBranch <= 210000:
    print ("\nNew York, NY, branch is: Open")
    time.sleep(1)
    print (ny_time.strftime('%m-%d-%Y %H:%M:%S'))
    time.sleep(2)
else:
    print ("\nNew York, NY, branch is: Closed")
    time.sleep(1)
    print (ny_time.strftime('%m-%d-%Y %H:%M:%S'))
    time.sleep(2)


london = timezone('Europe/London')
london_time = datetime.now(london)
londonBranch = int(london_time.strftime('%H%M%S'))

if londonBranch >= 9 and londonBranch <= 210000:
    print ("\nLondon, UK, branch is: Open")
    time.sleep(1)
    print (london_time.strftime('%m-%d-%Y %H:%M:%S'))
    time.sleep(2)
else:
    print ("\nLondon, UK, branch is: Closed")
    time.sleep(1)
    print (london_time.strftime('%m-%d-%Y %H:%M:%S'))
    time.sleep(2)

def normalHours():
    print ('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print ("Normal Business Hours: 9:00am - 9:00pm")
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    time.sleep(30)
normalHours()
