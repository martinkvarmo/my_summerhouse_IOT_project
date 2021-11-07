from network import LoRa
import socket
import time
import ubinascii

def connect_lora_socket():

    # Initialise LoRa in LORAWAN mode.
    # Please pick the region that matches where you are using the device:
    # Asia = LoRa.AS923
    # Australia = LoRa.AU915
    # Europe = LoRa.EU868
    # United States = LoRa.US915
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

    # create an OTAA authentication parameters, change them to the provided credentials
    app_eui = ubinascii.unhexlify('6081F9FF68E87979')
    app_key = ubinascii.unhexlify('B8078474D99CC4CCAEFE3B563AECB8E7')
    #uncomment to use LoRaWAN application provided dev_eui
    dev_eui = ubinascii.unhexlify('70B3D549957622C1')

    # Uncomment for US915 / AU915 & Pygate
    # for i in range(0,8):
    #     lora.remove_channel(i)
    # for i in range(16,65):
    #     lora.remove_channel(i)
    # for i in range(66,72):
    #     lora.remove_channel(i)

    # join a network using OTAA (Over the Air Activation)
    #uncomment below to use LoRaWAN application provided dev_eui
    #lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
    lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

    #pycom.rgbled(0xFF0000)  # Red

    # wait until the module has joined the network
    while not lora.has_joined():
        time.sleep(2.5)
        print('Not yet joined...')

    print('Joined')
    pycom.rgbled(0x00FF00)  # Green

    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    #host = 'dev.electra.se'
    #addr = socket.getaddrinfo(host,80)[0][-1]
    #s.connect(addr)
    #print('socket connected')

    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

    return s
