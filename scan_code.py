import os
import time

while True: 
        os.system('sudo python3 wifi_scan.py ./wifi_data -N 1');  #Just one loop in sudo command because we will be looping every 30 seconds
        os.system('sudo python3 ble_scan.py >> ble_data.txt'); #Add all the data at the end of the ble_data.txt file for every iteration
time.sleep(30);


