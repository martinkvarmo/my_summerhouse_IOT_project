

## My summerhouse surveillance IoT project

The purpose with the project is to surveillance power outage and temperature in a summerhouse on northern Öland. The house is empty for long periods, especially in the winter, and therefore it is interesting to see how the temperature varies and also see if there often is power outage. Actions will be taken dependent on the outcome of this project.

The main objective in participating in the course is to explore the IoT world and try to find out what benefits we can have from it in our company.

### Surveilence

##Assumption
When there power in the summerhouse it is possible to connect the Lopy4 to Wi-Fi, but when there is power outage the Wi-Fi is down and the Lopy4 is connected to Internet by LoRa. So that is mainly the way to detect when there is power outage.

##Connections
Data (date, temperature, wifi/lora) is posted to a service on Electra and stored in a database. The usage of an internal service makes it possible to take actions on different events, e.g. when LoRa network is used instead of wifi, or when the temperature is going below a certain level. We can send e.g. send email or SMS.

#LoRa/Helium
The Lopy4 device is setup in Helium and an integration is made with a service on Electra.

##Presentation

![image](https://user-images.githubusercontent.com/91141901/140646373-c2796a04-63bc-4d24-bb71-d68100b04e79.png)

### Material

![image](https://user-images.githubusercontent.com/91141901/140646210-71903b34-d8a9-414b-ad29-6fdb646d6eb2.png)

The material consists of
Lopy4 (https://pycom.io/product/lopy4/)
Expansion board 3.0 (https://pycom.io/product/expansion-board-3-0/)
Temperature sensor MCP9700
Batteri LiPo 3.7V 4400mAh
Breadboard (generic)
 Antenna
Jumper wire

The hardware is quite simple and the only things used, except from the Lopy4 and Expansion bord, is the MCP9700 temperature sensor. This is connected to ADC pin 15 on the expansion board.

The antenna is also connected to extend the range of LoRa.

### Environment setup

How is the device programmed. Which IDE are you using. Describe all steps from flashing the firmware, installing plugins in your favorite editor. How flashing is done on MicroPython. The aim is that someone should be able to understand how to reproduce your project.

- [ ] Chosen IDE
- [ ] How the code is uploaded
- [ ] Steps that you needed to do for your computer. Installation of Node.js, extra drivers, etc.

### Putting everything together

How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?

- [ ] Circuit diagram (can be hand drawn)
- [ ] Electrical calculations
- [ ] Limitations of hardware depending on design choices.
- [ ] Discussion about a way forward - is it possible to scale?

### Platforms and infrastructure

Describe your choice of platform(s). You need to describe how the IoT-platform works, and also the reasoning and motivation about your choices. Have you developed your own platform, or used 

Is your platform based on a local installation or a cloud? Do you plan to use a paid subscription or a free? Describe the different alternatives on going forward if you want to scale your idea.

- [ ] Describe platform in terms of functionality
- [ ] Explain and elaborate what made you choose this platform
- [ ] Provide a pricing discussion. What are the prices for different platforms, and what are the pros and cons of using a low-code platform vs. developing yourself?

### The code

Import core functions of your code here, and don't forget to explain what you have done. Do not put too much code here, focus on the core functionalities. Have you done a specific function that does a calculation, or are you using clever function for sending data on two networks? Or, are you checking if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, libraries and all that is needed to understand.


```python=
import this as that

def my_cool_function():
    print('not much here')

s.send(package)

# Explain your code!
```

### The physical network layer

How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.


- [ ] How often is the data sent? 
- [ ] Which wireless protocols did you use (WiFi, LoRa, etc ...)?
- [ ] Which transport protocols were used (MQTT, webhook, etc ...)
- [ ] Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.
- [ ] What alternatives did you evaluate?
- [ ] What are the design limitations of your choices?

### Visualisation and user interface

Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?

- [ ] Provide visual examples on how the visualisation/UI looks. Pictures are needed.
- [ ] How often is data saved in the database. What are the design choices?
- [ ] Explain your choice of database. What kind of database. Motivate.
- [ ] Automation/triggers of the data.
- [ ] Alerting services. Are any used, what are the options and how are they in that case included.

### Finalizing the design

Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

- [ ] Show final results of the project
- [ ] Pictures
- [ ] *Video presentation
