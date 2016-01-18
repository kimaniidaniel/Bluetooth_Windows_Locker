import bluetooth
import ctypes

target_name = "Xperia Z2"
nearby_devices = []
lock = True

try:
    nearby_devices = bluetooth.discover_devices(duration=10, lookup_names = True, flush_cache=True, lookup_class=False)
except:
    print "Issue with bluetooth lookup, halting"

for bdaddr, device_name in nearby_devices:
    print device_name, bdaddr
    services = bluetooth.find_service(address='44:74:6C:8B:65:C0')
    if target_name == device_name and len(services)>0:
        print "found target bluetooth device with address ", bdaddr
        lock = False
        break

if lock:
    print "Locking computer!"
    ctypes.windll.user32.LockWorkStation()
