## TCP Client

Create project from the esp-idf example project named `TCP Client example`. This should set up the tcp so you don't have to do it manually.

## TCP server

On a seperate terminal run the TCP server python script. Edit the IP and Port to your PCs info. Edit the filepath of where you want the data to be written.

## Configuring Wifi and TCP Client

In the `tcp_client.c` file configure your IP and Port number to match the server.

Setting up the wifi connection:

* run `idf.py menuconfig`.
* Select Example Connection Configuration.
* Scroll down to `Wifi SSID` and input your wifi SSID.
* Scroll down to `Wifi Password` and input your wifi password.
* Save and Quit.
