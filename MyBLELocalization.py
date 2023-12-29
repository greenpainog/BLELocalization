import matplotlib.pyplot as plt 
import numpy as np

import ScanUtility
import bluetooth._bluetooth as bluez

def trilaration(d1,d2,d3):
    """d1**2=x**2+y**2
    d2**2=((1-x)**2)+y**2
    d3**2=x**2+((1-y)**2)"""
    y = (d1**2+1-d3**2)/2
    value = d1**2 - y**2
    x = (value)**(1/2)
    
    
    return x, y
    
#synarthsh gia to vhma 3 
def distance(rssi, c, n):
    d = 10**((c-rssi)/(10*n))
    return d

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print ("\n *** Looking for BLE Beacons ***\n")
	print ("\n *** CTRL-C to Cancel ***\n")
except:
	print ("Error accessing bluetooth")

ScanUtility.hci_enable_le_scan(sock)
#Scans for iBeacons
i = 0
d1 = 0
d2 = 0
d3 = 0
x_vakues = [0, 1, 0]                    #periexei ola ta shmeioy toy x akswna
y_vakues = [0, 0, 1]
try:
	while True:
		returnedList = ScanUtility.parse_events(sock, 10)
        
		for item in returnedList:
			
                        #print("")
			#print("Beacon :",item["uuid"])
			u = item["uuid"]
			print("Beacon: ",u[0])
			print("rssi of beacon: ",item["rssi"])
			if u[0]  == "a":
				d1 = distance(item["rssi"], -62.81,  1.642)
				# plt.plot(0, 0, u[0])
				#print(u[0])
				
			elif u[0]  == "b":
				d2 = distance(item["rssi"], -62.81,  1.642)
				#print(u[0])
				# plt.plot(0, 1, u[0])
			else:
				d3 = distance(item["rssi"], -62.81,  1.642)
				#print(u[0])
				# plt.plot(1,0, u[0])
				
			if d1 and d2 and d3:
				coo = trilaration(d1,d2,d3)
				x = coo[0] #kaloyme mono to x
				y = coo[1] #antistoixa to y
				print("ras cooridates are:")
				print("X = ",x)
				print("Y = ",y)
				x_vakues.append(x)
				y_vakues.append(y)
				plt.scatter(x_vakues, y_vakues)
				
			plt.show()
			print("Distance from Pi is ",distance(item["rssi"], -62.81,  1.642),"metres")
			print("")
			print("\n")
			
except KeyboardInterrupt:
    pass
