The goals of the Mini-Project are to work with Raspberry Pi hardware and Python to use the Raspberry Pi as a wireless sensor for WiFi and Bluetooth.

After setting up the Raspberry Pi through installing the software onto the microSD card, the functions provided on the Senior Design Github page were utilized.
First, we collected nearby WiFi signals wirelessly using the Raspberry Pi. We collected data in BU's GSU and in the ECE Senior Design Lab for about 15 minutes each. The JSON file fron the GSU is included in **wifi_2021-09-15T11_36_16.json**, and the JSON file from the ECE Lab is in **wifi_2021-09-16T13_34_30.json**. 


Once the scanning was complete, the data was saved to a JSON file which we saved to our Laptop's Desktop. We initally tried to copy the file over SSH; however, we could not get the command to work correctly. Therefore, we copied the JSON files via Google Drive.
After copying the files to our laptop's desktop, we were able to run the function **wifi_scan.py** in our laptop's terminal.

Additionally, we created the script **scan_code.py** so that the wifi scanning and bluetooth scanning could be done all at once.

GSU Result:
![Figure_1](https://user-images.githubusercontent.com/55505652/133662423-a322d3da-cd5d-4e0f-8ef1-e844e4ca7895.png)

ECE Lab Result:
![Figure_2](https://user-images.githubusercontent.com/55505652/133662450-d2283e5e-bba1-4a01-827c-caf6bbd4fd0c.png)

Overall, working with the Raspberry Pi hardware along with navigating how to control it in the terminal were useful skills for going forward.
