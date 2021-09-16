import os
import time

while True: 
        os.system('sudo python3 wifi_scan.py ./wifi_data -N 1');
        os.system('sudo python3 ble_scan.py >> ble_data.txt');
time.sleep(30);


