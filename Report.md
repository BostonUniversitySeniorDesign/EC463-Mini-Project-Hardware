The goals of the Mini-Project are to work with Raspberry Pi hardware and Python to use the Raspberry Pi as a wireless sensor for WiFi and Bluetooth.

After setting up the Raspberry Pi through installing the software onto the microSD card, the functions provided on the Senior Design Github page were utilized.
First, we collected nearby WiFi signals wirelessly using the Raspberry Pi. We collected data in BU's GSU and in the ECE Senior Design Lab. The JSON file fron the GSU is included in [wifi_2021-09-15T11_36_16.json](wifi_2021-09-15T11_36_16.json), and the JSON file from the ECE Lab is in [wifi_2021-09-16T13_34_30.json](wifi_2021-09-16T13_34_30.json). We also did another WiFi scan in the ECE Senior Design Lab for over 30 minutes with its data included in [wifi_2021-09-16T14_07_54.json](wifi_2021-09-16T14_07_54.json).


Once the scanning was complete, the data was saved to a JSON file which we saved to our Laptop's Desktop. We initally tried to copy the file over Secure Copy (scp); however, we could not get the command to work correctly. Therefore, we copied the JSON files via Google Drive. To being able to copy the files while not being in the lab (with the monitor+keyboard set up) we found another way that worked to copy the files from Raspberry Pi to Mac via SSH File Transfer Protocol (sftp).
After copying the files to our laptop's desktop, we were able to run the function [wifi_scan.py](wifi_scan.py) in our laptop's terminal.

Although in the wifi file we could specify the number of loops in the N parameter, in the bluetooth file we couldn't, that's why we created the script [scan_code.py](scan_code.py) so that the wifi scanning and bluetooth scanning could be done all at once without having to run ourselves the bluetooth command every minute/half a minute.

GSU Result:
![Figure_1](https://user-images.githubusercontent.com/55505652/133662423-a322d3da-cd5d-4e0f-8ef1-e844e4ca7895.png)

ECE Lab Result (15 minutes):
![Figure_2](https://user-images.githubusercontent.com/55505652/133662450-d2283e5e-bba1-4a01-827c-caf6bbd4fd0c.png)

ECE Lab Result (50+ minutes):
![Figure_3](https://user-images.githubusercontent.com/55505652/133671432-0338ecb7-63a0-4f0c-a3fb-fbbf4fe74978.png)




As shown in the graphs, the amount of BSSIDs seen across time fluctuates. There was more activity shown in the GSU than in the ECE lab. In the GSU, there was a greater maximum of 8 BBSIDs than in the ECE lab of 7 and then 5. Additionally, the GSU's data never hit zero after the beginning of the scan, wheresas in the ECE lab, the amount of new BSSIDs hit zero many times throughout the duration of the scan. When the Raspberry Pi scanned for the longer duration, the graph and trends are shown clearer and more accurately. The average of new BSSIDs comes to around 1. In the data with the shorter scan time, the average is less accurate.

Overall, working with the Raspberry Pi hardware along with navigating how to control it in the terminal were useful skills for going forward.
