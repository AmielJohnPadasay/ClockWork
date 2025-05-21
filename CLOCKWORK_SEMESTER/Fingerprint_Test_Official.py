from pyzkfp import ZKFP2


zkfp2 = ZKFP2()
zkfp2.Init() # Initialize the ZKFP2 class

# Get device count and open first device
device_count = zkfp2.GetDeviceCount()
print(f"{device_count} devices found")
zkfp2.OpenDevice(0) # connect to the first device