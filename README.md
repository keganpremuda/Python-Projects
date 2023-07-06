<h1>Python Project Collection</h1>

<h2>Description</h2>
This collection consists of various projects that demonstrate my abilities with Python, and my understanding of coding for real-time applications.
<br />


<h2>Languages Used</h2>

- <b>Python</b> 

<h2>Environments Used </h2>

- <b>Nano</b> (Raspberry Pi OS)

<h2>Equipment Used</h2>

- <b>Raspberry Pi 4</b>

<h2>Electrical Components Used</h2>

- <b>RGB LED</b>
- <b>White LED</b>
- <b>Button Switches</b>
- <b>Breadboard</b>
- <b>Analog Parts Kit</b>

<h2>Collection walk-through:</h2>

<p align="center">
<b>Analog RGB Hue Modifier:</b><br/>
<a href="https://github.com/keganpremuda/PythonProjects/blob/main/analogRGBButton.py">analogRGBButton.py</a><br></p>
<p align="left">
This program takes inputs from three switches that represent the red, green, and blue hue intensities that an RGB LED will emit as an output, and then displays those values in the terminal.
The connection between the circuit and the pins on the Raspberry Pi 4 was achieved using the Rpi.GPIO library, and for this circuit, the switches were implemented using internal Raspberry Pi 4 pull-up resistors.
The project also uses a Virtual Python library to simulate the change in RGB LED hue in a simulation window as the LED changes hue in real time. The Virtual Python simulation is used as
digital validation that the code is functioning as intended.</p>
<br />
<br />
<p align="center">
<b>Analog LED Brightness Modifier:</b><br/>
<a href="https://github.com/keganpremuda/PythonProjects/blob/main/brightDimButtons2.py">brightDimButtons2.py</a><br></p>
<p align="left">
This program takes in inputs from two switches that control the brightness of an LED and then displays the brightness value in the terminal.
The program alerts the terminal when the brightness values are at their maximum and minimum values.
The brightness increments by the power of a number to adjust for the large jumps in perceived brightness as the brightness changes at lower voltages.
The connection between the circuit and the pins on a Raspberry Pi 4 was achieved using the Rpi.GPIO library, and for this circuit, the switches were implemented using internal Raspberry Pi 4 pull-up resistors.
Pulse width modulation was utilized to achieve analog values for the output of the LED.</p>
<br />
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
