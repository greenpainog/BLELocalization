# BLE iBeacon Scanner
 A simple project that scans for  BLE beacons using your Raspberry Pi with Python. 
# Getting Started
You will need to download bluez to get bluetooth data.
- sudo apt-get update.
- sudo apt-get install python-pip python-dev ipython
- sudo apt-get install bluetooth libbluetooth-dev
- sudo pip install pybluez
> Additionally to detect BLE devices you need to enable the experimental features. To do this:
1. Go to directory
- cd /lib/systemd/system
2. Edit a file
- sudo vim bluetooth.service
> Add --experimental after ExecStart=/usr/local/libexec/bluetooth/bluetoothd So it lookes like this:

ExecStart=/usr/local/libexec/bluetooth/bluetoothd --experimental
3. Save and exit vim Shift + Colon, then type wq! - to write and quit.

4. Restart daemon

> sudo systemctl daemon-reload
5. Restart bluetooth
> sudo systemctl restart bluetooth
> 
# Quick Start
Download files.

Go to directory
> cd Desktop/BLE-Beacon-Scanner

Run

python BeaconScanner.py

# Running the tests
Once the app is running you should see any iBeacon in the vicinity - The RSSI will update if an iBeacon moves.
A pop up window will shouw up showing a live coordinated map with your BLE Beacons around your Raspberry Pi device.

