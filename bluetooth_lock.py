import bluetooth
import ctypes

"""
To use this tool change the your_device_bluetooth_name to
your device blueooth name - you should be able to find this
in your device's bluetooth settings
"""
#--------------Change Here--------------
your_device_bluetooth_name = "Xperia Z2"
#---------------------------------------


nearby_devices = []
lock = True
try:
    nearby_devices = bluetooth.discover_devices(duration=10, lookup_names = True, flush_cache=True, lookup_class=False)
except:
    print "Issue with bluetooth lookup, halting"

for bdaddr, device_name in nearby_devices:
    #print device_name, bdaddr #<--for debugging
    services = bluetooth.find_service(address=bdaddr)
    if your_device_bluetooth_name == device_name and len(services)>0:
        print "found",your_device_bluetooth_name,"with address", bdaddr
        lock = False
        break

if lock:
    print "Locking computer!"
    ctypes.windll.user32.LockWorkStation()
