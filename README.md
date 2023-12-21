# BIN2ASCII
BIN2ASCII is a background python script which converts any binary inside the Arduino Serial and gives out the Corresponding ASCII Value and automatically types it using the keyboard library.
## Intented uses
BIN2ASCII is a script which is meant to be used to have something like the keyboard library in the Arduino IDE but instead to support any arduino which isnt supported by the keyboard library from the Arduino IDE. When possible its more recommended to use the library from the Arduino IDE instead of this script.
# Important!
- BIN2ASCII is based on linux distros so the serial Port is set to /dev/ttyCH341USB0, please change this to your corresponding port for your Arduino Chip and Operating System!
- port.py is an example i made with my Arduino. Its basically a keyboard which i can type in the 0 and 1 and it will print it on my Serial which my python script will understand
- Theres been a few issues with the Keyboard library being unable to type some characters. If you find any fix feel free to edit my script!
