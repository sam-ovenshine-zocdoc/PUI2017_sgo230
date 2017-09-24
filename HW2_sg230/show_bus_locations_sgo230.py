
# coding: utf-8

# In[2]:


from __future__ import print_function
# the next import allows me to read line input arguments
import sys
import requests
import os

if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_sgo230.py <MTA_KEY> <BUS_LINE>")
    sys.exit()


# In[3]:


# Configuration
token = sys.argv[1]
line = sys.argv[2]


# In[4]:


resp = requests.get('http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + token + '&VehicleMonitoringDetailLevel=calls&LineRef=' + line)
resp = resp.json()
buses = resp['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
buses_count = len(buses)


# In[5]:


print('Bus Line : ' + line + '\nNumber of Active Buses : ' + str(buses_count))
for elem in range(buses_count):
    print('Bus ' + str(elem) + ' is at latitude ' +
          str(buses[elem]['MonitoredVehicleJourney']['VehicleLocation'].values()[0]) +' and longitude ' + 
          str(buses[elem]['MonitoredVehicleJourney']['VehicleLocation'].values()[1])
         )


# In[6]:


for elem in range(buses_count):
    try:
        print(
            str(buses[elem]['MonitoredVehicleJourney']['VehicleLocation'].values()[0]) + ',' +
            str(buses[elem]['MonitoredVehicleJourney']['VehicleLocation'].values()[1]) + ', ' +
            buses[elem]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'] + ', ' +
            buses[elem]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
             )
    except:
        print(
            str(buses[elem]['MonitoredVehicleJourney']['VehicleLocation'].values()[0]) + ',' +
            str(buses[elem]['MonitoredVehicleJourney']['VehicleLocation'].values()[1]) + ', ' +
            'N/A, N/A'
             )

