import pywifi

# Initialize the WiFi interface
wifi = pywifi.PyWiFi()

# Get the first available WiFi interface
interface = wifi.interfaces()[0]

# Disconnect from the current network (if connected)
if interface.status() == pywifi.const.IFACE_CONNECTED:
    interface.disconnect()

# Scan for available WiFi networks
interface.scan()

# Get the list of WiFi networks
networks = interface.scan_results()

# Iterate through the networks
for network in networks:
    # Get the SSID (name) of the network
    ssid = network.ssid

    # Attempt to connect to the network
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = pywifi.const.AUTH_ALG_OPEN
    profile.akm.append(pywifi.const.AKM_TYPE_NONE)

    # Connect to the network
    interface.remove_all_network_profiles()
    tmp_profile = interface.add_network_profile(profile)
    interface.connect(tmp_profile)

    # Check if the connection was successful
    if interface.status() == pywifi.const.IFACE_CONNECTED:
        print(f"Successfully connected to {ssid}")
        # TODO: Extract password information
        # Note: Password extraction is not supported by pywifi
        # You would need to use other methods or libraries for password cracking

    # Disconnect from the network
    interface.disconnect()

# Disconnect from the current network (if connected)
if interface.status() == pywifi.const.IFACE_CONNECTED:
    interface.disconnect()