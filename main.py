from network import LoRa
import socket
import time
import ubinascii
from lora_help import connect_lora_socket

import pycom # "pycom" will be an error in your
# IDE because it's not on your computer, but on
# the device
import time
import machine

from machine import ADC
from machine import Pin
from network import WLAN
import socket

#LoRa
#from network import LoRa
#import binascii
#print(binascii.hexlify(LoRa().mac()).upper())

pycom.heartbeat(False)
pycom.rgbled(0x0000FF) # blue
#time.sleep(2) #sleep for 1 second

##====== LoRa ======

## Initialise LoRa in LORAWAN mode.
## Please pick the region that matches where you are using the device:
## Asia = LoRa.AS923
## Australia = LoRa.AU915
## Europe = LoRa.EU868
## United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an OTAA authentication parameters, change them to the provided credentials
app_eui = ubinascii.unhexlify('6081F9FF68E87979')
app_key = ubinascii.unhexlify('B8078474D99CC4CCAEFE3B563AECB8E7')
#uncomment to use LoRaWAN application provided dev_eui
dev_eui = ubinascii.unhexlify('70B3D549957622C1')

## Uncomment for US915 / AU915 & Pygate
## for i in range(0,8):
##     lora.remove_channel(i)
## for i in range(16,65):
##     lora.remove_channel(i)
## for i in range(66,72):
##     lora.remove_channel(i)

## join a network using OTAA (Over the Air Activation)
##uncomment below to use LoRaWAN application provided dev_eui
##lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
#lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

#pycom.rgbled(0xFF0000)  # Red

## wait until the module has joined the network
#while not lora.has_joined():
#    time.sleep(2.5)
#    print('Not yet joined...')

#print('Joined')
#pycom.rgbled(0x00FF00)  # Green

## create a LoRa socket
#s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

## set the LoRaWAN data rate
#s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

##====== End LoRa ======

#====== WiFi ======

wlan = WLAN(mode=WLAN.STA)

#wlan.connect(ssid='Electra.ans', auth=(WLAN.WPA2, '543rt5my'))
#wlan.connect(ssid='itr6800', auth=(WLAN.WPA2, '2l8nites4U'))
wlan.connect(ssid='Stargate_IoT', auth=(WLAN.WPA2, 'TieFighter'))
#wlan.connect(ssid='Martins iPhone', auth=(WLAN.WPA2, 'j1aqdr2q2heb9'))
#while not wlan.isconnected():
#    print("WiFi not connected")
#    time.sleep(2) #sleep for 2 seconds
#    machine.idle()

time.sleep(5) #sleep for 5 seconds

#====== End WiFi ======

data = ''
adc = ADC()
tempsensor = adc.channel(pin='P15')   # create an analog pin on P15
bat_voltage = adc.channel(attn=ADC.ATTN_11DB, pin='P16')

while True: #Forever loop

    vbat = bat_voltage.voltage()*2
    # note that the expansionboard 3 has a voltage divider of 1M / 1M to account for
    # 1M / 1M, ratio = 1:2

    millivolts = tempsensor.voltage() # Analog temperature measured in millivolts
    degC = (millivolts - 500.0) / 10.0 # Convert millivolts to celsius
    degF = ((degC * 9.0) / 5.0) + 32.0 # Convert celsius to fahrenheit

    print('battery voltage:', vbat, 'mV')
    print('temperature:', degC, ' C')

    if vbat >= 4420:
        pycom.rgbled(0x00FF00)  # Green
    else:
        pycom.rgbled(0xFF0000)  # Red

    if wlan.isconnected():

        print("WiFi connected")
        time.sleep(5) #sleep for 5 seconds
        print(wlan.ifconfig())

        # setup socket for connection
        wifi_socket = socket.socket()
        #s = ssl.wrap_socket(s)
        host = 'dev.electra.se'
        addr = socket.getaddrinfo(host,80)[0][-1]
        wifi_socket.connect(addr)
        print('socket connected')

        data = '2,' + str(vbat) + ',' + str(degC) + ',' + '4'
        httpreq = 'POST /MessageHandler.ashx HTTP/1.1 \r\nHOST: '+ host + '\r\nContent-Length: ' + str(len(data)) + '\r\nConnection: keep-alive \r\n\r\n' + data
        print('http request: \n', httpreq)
        wifi_socket.send(httpreq)
        rec_bytes = wifi_socket.recv(10000)
        print(rec_bytes)
    else:
        print("WiFi not connected")

        # Try to join LoRa
        if not lora.has_joined():
            # join a network using OTAA (Over the Air Activation)
            #uncomment below to use LoRaWAN application provided dev_eui
            #lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
            lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

            # wait until the module has joined the network
            while not lora.has_joined():
                time.sleep(2.5)
                print('LoRa not yet joined...')

            # create a LoRa socket
            lora_socket = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

        #else:
            #lora_socket = connect_lora_socket()

        print('LoRa joined')

        ## send some data
        data = '2,' + str(vbat) + ',' + str(degC) + ',' + '3'
        lora_socket.send(data)

    #time.sleep(600) #sleep for 10 minutes
    time.sleep(10) #sleep for 10 seconds
