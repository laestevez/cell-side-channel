## Setup
* Look at `wiring.png` for a wiring diagram.
* The USB-C wire was spliced with the ground wire being cut.
* The VP pin uses ADC1_CHANNEL0 which the code configures.
* The wifi setup below uses VSCode ESP-IDF Extension.

## TCP Client

Create project from the esp-idf example project named `TCP Client example`. This should set up the tcp so you don't have to do it manually.

## TCP server

On a seperate terminal run the TCP server python script. Edit the IP and Port to your PCs info. Edit the filepath of where you want the data to be written.
The python script passes a 4 digit pin as a command line argument, Then writes it at the top of the file when connected to the board.

## Configuring Wifi and TCP Client

In the `tcp_client.c` file configure your IP and Port number to match the server.

Setting up the wifi connection:

* run `idf.py menuconfig`.
* Select Example Connection Configuration.
* Scroll down to `Wifi SSID` and input your wifi SSID.
* Scroll down to `Wifi Password` and input your wifi password.
* Save and Quit.

## Graphing Libraries needed

* run `pip install numpy`.
* run `pip install matplotlib`

## Parts List
| Part      | URL |
| ----------- | ----------- |
| Microcontroller: ESP32-DEVKITC-DA      | https://www.digikey.com/short/ttn8v10n  |
| USB Cable: CA-USB-AM-CM-3FT   | https://www.digikey.com/short/pr9v50qn  |
| MBreadboard: PRT-12614     | https://www.digikey.com/en/products/detail/sparkfun-electronics/PRT-12614/17828082  |
| Resistors: KNP1WSJR-52-0R1   | https://www.digikey.com/en/products/detail/yageo/KNP1WSJR-52-0R1/2812996  |
