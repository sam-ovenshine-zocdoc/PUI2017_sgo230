
# coding: utf-8

# In[2]:


from __future__ import print_function
# the next import allows me to read line input arguments
import sys
import requests
import os

#if not len(sys.argv) == 4:
#    print ("Invalid number of arguments. Run as: python get_bus_info_sgo230.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
#    sys.exit()


# In[3]:


# Configuration
token = sys.argv[1]
line = sys.argv[2]
output = sys.argv[3]


# In[4]:


resp = requests.get('http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + token + '&VehicleMonitoringDetailLevel=calls&LineRef=' + line)
resp = resp.json()
buses = resp['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
buses_count = len(buses)


# In[21]:


fout = open(output, "w")

fout.write('Latitude,Longitude,Stop Name,Stop Status\n')

for elem in range(buses_count):
    try:
        fout.write(
            str(buses[elem]['MonitoredVehicleJourney']['VehicleLocation'].values()[0]) + ',' +
            str(buses[elem]['MonitoredVehicleJourney']['VehicleLocation'].values()[1]) + ',' +
            buses[elem]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'] + ',' +
            buses[elem]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'] +
            '\n'
             )
    except:
        fout.write(
            str(buses[elem]['MonitoredVehicleJourney']['VehicleLocation'].values()[0]) + ',' +
            str(buses[elem]['MonitoredVehicleJourney']['VehicleLocation'].values()[1]) + ',' +
            'N/A,N/A' +
            '\n'
             )

