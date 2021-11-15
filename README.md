

# My summerhouse surveillance IoT project

The purpose with the project is to surveillance power outage and temperature in a summerhouse on northern Öland. The house is empty for long periods, especially in the winter, and therefore it is interesting to see how the temperature varies and also see if there often is power outage. Actions will be taken dependent on the outcome of this project.

### Surveillance

#### Assumption
When there is power in the summerhouse it is possible to connect the Lopy4 to wifi, but when there is power outage the wifi is down and the Lopy4 is connected to Internet by LoRa. So that is mainly the way to detect when there is power outage.

#### Software
The Lopy4 will be connected to a wifi access point and the access point will be connected to Internet by 4G.

At start the Lopy4 will be connected to the wifi, and once a minute it will be woken up, the temperature will be measured and the data will be sent to the service. If the connection is lost, it will instead try to connect to LoRa. The data sent to the service will indicate wether wifi or LoRa was used for transmitting the data. 

Note. LoRa network coverage has not been tested at the site, it's just an assumption that there is coverage. If the coverage is poor, we can develop the service to send an alarm when no data has been uploaded during the last x minutes.

#### Connections/service
Data (date, temperature, wifi or lora used) is posted to a ASHX web service, hosted by Electra, and stored in a database. The usage of an internal service makes it possible to take actions (e.g. send email or SMS) on different events, e.g. when LoRa network is used instead of wifi, or when the temperature is going below a certain level.

#### Power supply
The Expansion board is mainly powered by USB and a battery as backup in case of power outage.

#### LoRa/Helium
The Lopy4 device is setup in Helium and integrated with a service on Electra.

### Presentation

![image](https://user-images.githubusercontent.com/91141901/140646373-c2796a04-63bc-4d24-bb71-d68100b04e79.png)

The temperature will be displayed in a BI report.

### Material

![image](https://user-images.githubusercontent.com/91141901/140646210-71903b34-d8a9-414b-ad29-6fdb646d6eb2.png)

We bought a "LoPy4 and sensors bundle" from Elektrokit (https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-lopy4-and-sensors-bundle/) and completed this with battery (https://www.electrokit.com/produkt/batteri-lipo-3-7v-4400mah/).

The material used in the project consists of:

Lopy4 (https://pycom.io/product/lopy4/)

Expansion board 3.0 (https://pycom.io/product/expansion-board-3-0/)

Temperature sensor MCP9700

Batteri LiPo 3.7V 4400mAh (249 kr)

Breadboard (generic)

Antenna

Jumper wire

The hardware is quite simple and the only things used, except from the Lopy4 and Expansion bord, is the MCP9700 temperature sensor. The sensor is connected to ADC pin 15 on the expansion board.

An antenna is also connected to extend the range of LoRa.
