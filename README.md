<p align="center"><img src ="https://github.com/pycom/pycom-libraries/blob/master/img/logo.png" width="300"></p>

# Getting Started with the SiPy and Sending Data
Welcome! This workshop help you get up and running with MicroPython and the Pycom SiPy. This workshop is written directly parallel to the Microsoft and Sigfox elements for the 19th of June Sigfox + Microsoft + Pycom workshop in San Francisco, USA.

<p align="center"><img src ="https://github.com/pycom-education/pycom-workshop-sf/blob/master/images/SiPy.png" width="300"></p>

**Warning!**
Before you get started with the tutorial please follow the [instructions](https://docs.pycom.io/pycom_esp32/pycom_esp32/getstarted.html#firmware-upgrades) for updating the firmware on your device. Thanks!

# Table of Contents
* [What You'll Need](#What-You'll-Need)
* [Getting Started](#Getting-Started)
* [Next Steps](#Next-Steps)
* [Sigfox Part](#Sigfox-Part)
* [Extra Information](#Extra-Information)
* [Useful Links](#Useful-Links)
* [Contributing](#Contributing)

# What You'll Need
To make the most out of this workshops, you'll need the following:

* Pycom SiPy (22 dBm for USA)
* Pycom Expansion Board
* Windows/MacOS/Linux Computer (Laptop, PC, etc.)
* Atom Text Editor (+ Pymakr Plugin)
* Micro USB Cable
* Male to Male Jumper Wire (Used to update the SiPy)

# Getting Started
In this workshop we'll look at MicroPython concepts, experiment with reading data from a temperature sensor and using the Sigfox Network to send the temperature data.

### **Important - Update Your Firmware!**

Before you start this workshop, it's important that you update your device to be running the latest build of our firmware. This will ensure that the latest features are available and that anything reference to in this workshop, will work exactly the same on your device as on the device of the presenter!

Please download the [firmware update tool](https://www.pycom.io/downloads/) and install the tool for your specific operating system.

You'll need to use a jumper wire to connect across pins GND and G23, as seen on the expansion board. When the pins are connected, power on the SiPy (plug the micro USB cable into your computer) and it will boot into Firmware Upgrade Mode. You'll need to specify the country which you are using the device (i.e. USA). 

<p align="center"><img src ="https://github.com/pycom-education/pycom-workshop-sf/blob/master/images/update.png" width="500"></p>

Once your device is successfully updated, you'll be greeted with a final screen that tells your the SiPy's Sigfox PAC and ID. Remove the jumper wire after a successfully update.

<p align="center"><img src ="https://github.com/pycom-education/pycom-workshop-sf/blob/master/images/update-sigfox.png" width="500"></p>

**Save the Sigfox PAC and ID as you'll need them for registering your device later.**

#### MicroPython Concepts

If you have used Python 3 previously, MicroPython (MP) should seem familiar to you! If not, you'll have no problems getting started as Python is a fantastic language with syntax that is very similar to english.

Lets take a look at some examples but first lets get set up to test some code on the SiPy!

#### Testing Your Code!

To test your code, we'll use the MicroPython REPL (Read Evaluate Print Line) Console. This lets us directly talk to the MP Interpreter, which is used to run code on the SiPy.

### Pymakr Plugin

The easiest way to interact with a Pycom device is by using our Pymakr Plugin. Currently this is available for the Atom code editor but will be more widely available at a later date.

Navigate to https://atom.io to download the Atom text editor and then locate **preferences** -> **install**, then search for **Pymakr**.

Install the plugin and click the **open** button at the bottom of the window. That's it, you're ready to go!

#### Connecting your SiPy

Now that Pymakr is installed, you can connect it to your device by clicking the **connect** button in the Pymakr Console. If your device isn't found immediately, you might need to add the device's serial address inside the settings. Click **more** and then **get serial ports**. This will list out all of the available serial ports and copy the Pycom device to your clipboard. Now navigate to the **global settings**, via the **settings** button. You'll now see a text box for device address; paste your clipboard here and the  click **reconnect** (in the Pymakr Console).

#### Getting Started Examples

You should now be ready to try out some examples! Once you've connected to your SiPy, you'll see three arrows (```>>>```) in the console. These let you know that you're in the MicroPython REPL! If you don't see the indicators, please press the reset button (next to the LED) on your SiPy.

To start we'll just try some simple creating & storing variables.

Below, we create a variable named 'value' and are storing the string "Hello World" inside of it. We can next print this value back to our screen with the 'print()' function!

```python
>>> value = "Hello World"
>>> print(value)
```

You can also do arithmetic and control flow as well as looping your code!

```python
>>> x = 0
>>> for y in range(0,9):
>>> 	x += 1
>>> print(x)
```

There are some more examples in the [Examples](/examples) Folder.

**Note** - Python (and MicroPython) are whitespace dependent, this means you need to specify code hierarchy using 4 spaces (or a single tabs). Everything within the *for loop* should be indented by 4 spaces. This lets the Python interpreter know which code to run and when!

If you want to learn more about the Python Programming Language, check out [these](https://www.tutorialspoint.com/python/) tutorials!

We're now going to get into specific that relate to the SiPy Boards and accessing its hardware features!

### Flashing an LED

One of the first things many beginners do when they learn about MicroControllers, is to blink an LED.

We're going to use a different method of running our code on the Pycom Devices this time.

#### Uploading Code to Your Device (via Pymakr Plugin)

Earlier, we ran code live on the device using the Python REPL. Now we'll upload complete programs that will be loaded to the device so that it will run every time upon boot!

#### Write Your Code!

Now that we're ready to upload some code to the board, we can finally start writing some code! Let start with a simple main.py file to blink the LED for us.

**Note** - MicroPython starts up and runs a file named **boot.py**. Once this has executed, another file **main.py** then runs. We can use **boot.py** to set up our device config, such as WiFi or UART and then put our main program/logic into the **main.py** file.

We will use a library known as 'pycom' to control the onboard LED and another library called 'time' to manage the blinking. The board also blinks by default so we'll change the colour and disable the default blinking behaviour!

```python
import time
import pycom

# We need to disable to the default blinking!
pycom.heartbeat(False)

# Loop to run this code forever
while True:
    # Set the RGB LED to Green
    pycom.rgbled(0x00FF00)
    # Sleep the board for 1 second
    time.sleep(1)
    # Set the RGB LED to Off
    pycom.rgbled(0x000000)
    time.sleep(1)
```

To run this in the REPL, without having to type it all by hand, you can use the **run** button in Pymakr. This performs the same steps as entering code by hand, except that it reads from a file and automatically enters the code.

In order to ensure you've got an empty directory for uploading your code, create a new project for your code and remove any existing projects that you might have open. Once you've saved this file as **main.py**, ensure that you're connect to your device via Pymakr then click **Sync**.

This will upload any files inside of the directory to your device. You can specify certain files via a pymakr.conf file if you wish.

### Collecting Temperature Sensor Data

Next we'll look at using a temperature (DS18B20), to collect some information about your surroundings. We'll use a library for the specific sensor, store the data and then send it over Sigfox.

To begin, navigate to the [libraries](/libraries) and download the file **onewire.py**. This contains the instructions required for your program to retrieve data from the sensor.

We'll next want to create a structured directory on our SiPy so that the MicroPython interpreter knows where to find the library files.

Inside your project folder, create a new folder called **lib** and place the **onewire.py** file inside **lib**. Your project should now looks like this:

- Project/
    - lib/
        - onewire.py
    - main.py
    - boot.py

We can retrieve the code from **onewire.py** using the command ```import onewire```.

To start, connect your temperature sensor to your SiPy as shown in the picture below. You'll need to connect the sensor to Pin 10, GND and 3v3.

Next we'll write a function that get the temperature data and then look at how to send it over Sigfox.

#### Writing the Temperature Sensor Function

The temperature sensor library makes it very easy to start collecting data. Ensure that your **main.py** file is empty and is ready to be written to.

```Python
import time
from machine import Pin
from onewire import DS18X20
from onewire import OneWire

#DS18B20 data line connected to pin P10
ow = OneWire(Pin('P10'))
temp = DS18X20(ow)

def getTemp():
    temp.start_convertion()    
    time.sleep(1)
    return temp.read_temp_async()

print(getTemp())
```

You can remove the ```print(getTemp())``` statement when you have finsihed testing your code. Now we'll take a look at the Sigfox aspect of sending your data.

### Sending Your Data over Sigfox

The Sigfox libraries already exist onboard the SiPy so you can import them using the following command, without having to download any additional files.

You'll need to specify some configuration and then we can write the send message function. The newly added Sigfox code is followed by a comment.

```python
import time
from machine import Pin
from onewire import DS18X20
from onewire import OneWire
from network import Sigfox # import the Sigfox Library
import socket # import the socket connection library

ow = OneWire(Pin('P10'))
temp = DS18X20(ow)

sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ2) # initialise the Sigfox Radio and set it for US region
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW) # create a Sigfox socket
s.setblocking(True) # set the socket to blocking
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False) # set the socket to uplink only

def getTemp():
    temp.start_convertion()    
    time.sleep(1)
    return temp.read_temp_async()
```

Once the Sigfox radio has been setup, we'll next need to convert the message into hexadecimal format and send it over Sigfox. We can do this by adding another function that takes in the value we retrieved from the temperature sensor and sends it via Sigfox.

```python
import time
from machine import Pin
from onewire import DS18X20
from onewire import OneWire
from network import Sigfox # import the Sigfox Library
import socket # import the socket connection library

ow = OneWire(Pin('P10'))
temp = DS18X20(ow)

sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ2) # initialise the Sigfox Radio and set it for US region
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW) # create a Sigfox socket
s.setblocking(True) # set the socket to blocking
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False) # set the socket to uplink only

def getTemp():
    temp.start_convertion()    
    time.sleep(1)
    return temp.read_temp_async()

def sendSigfox(data):
    s.send(data)
```

Finally, we'll add a main() function to call all of our other functions inside of a loop. The code below will run through the loop, collecting temperature data, sending it via Sigfox then pausing the device for 10 minutes until it's ready to send data again (In accordance to LPWAN protocols).

```python
import time
from machine import Pin
from onewire import DS18X20
from onewire import OneWire
from network import Sigfox # import the Sigfox Library
import socket # import the socket connection library

ow = OneWire(Pin('P10'))
temp = DS18X20(ow)

sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ2) # initialise the Sigfox Radio and set it for US region
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW) # create a Sigfox socket
s.setblocking(True) # set the socket to blocking
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False) # set the socket to uplink only

def getTemp():
    temp.start_convertion()    
    time.sleep(1)
    return temp.read_temp_async()

def sendSigfox(data):
    s.send(data)

def main():
    while True:
        temperature = getTemp()
        sendSigfox(temperature)
        time.sleep(600)

main()
```

**There are two important notes here.** Firstly, ensure that you have an antenna connected to your SiPy before attempting to send a Sigfox message as this can damage the device otherwise. Secondly, you will not be able to see any of your Sigfox messages until you have registered your device with the Sigfox Backend. This will be explained to you in the Sigfox section of this workshop.

### Finished - Viewing Your Data via Sigfox Backend

That's the end of the Pycom section of this workshop! The Sigfox team will now walk you through registering your SiPy on their network and viewing the incoming data from your SiPy. From this point on, you'll be able to connect Sigfox into Microsoft's Azure platform and visualise your data!


Thanks for participating and let us know if you have any questions/suggestions!

---

### Additional Information

Here are some extra tips for taking your SiPy further and making use of all of it's available hardware!

#### Connecting Your Device to Your Own WiFi Network

This example shows to connect to a WiFi address. It uses the 'WLAN' class from the 'network' library.

```python
from network import WLAN

wlan = WLAN(mode=WLAN.STA) # Create WLAN Object

nets = wlan.scan() # Scans for available networks
for net in nets:
    if net.ssid == 'your-wifi-name':
        print('Network found!') # Prints string if network is found!
        wlan.connect(net.ssid, auth=(net.sec, 'your-wifi-password'), timeout=5000)
        while not wlan.isconnected():
            machine.idle()
        print('WiFi Connected!')
        break
```

Paste this into your boot.py file and set your Pycom Device to automatically connect to your WiFi network each time it turns on.


# Sigfox Part
## Registering your device
You will need to register your device on the sigfox network.
To do so, go to https://backend.sigfox.com/activate, select the devkit Pycom, select the country USA, fill in the device information (device ID and PAC provided earlier by the Pycom software), fill in your account information.
You have just created your developper account on the sigfox backend.

## Sigfox backend
You should have received an email to create your password.
You will find tutorials on the sigfox backend at https://www.youtube.com/playlist?list=PLcw1TnahFRW-dpqGwxa3noSMLP_nTEhdb

## Create your Microsoft Azure account and configure the Sigfox backend 
You will need to create your Microsoft Azure account before configurung the Sigfox backend.
You will find the step by step process to do so at https://github.com/aureleq/sigfox-azure-iothub
When configuring the sigfox backend make sure to configure as shown below:
<p align="center"><img src ="https://github.com/francoisoudot/pycom-workshop-sf/blob/patch-1/images/Screen%20Shot%202017-06-15%20at%2013.01.14.png" width="500"></p>


# Useful Links
* [Pycom](https://pycom.io)
* [Forum](https://forum.pycom.io)
* [Documentation](https://docs.pycom.io)

# Contributing
Please see the [contribution guide](CONTRIBUTE.md) for how you can add your resources back into the community and how to contribute to this repository.
