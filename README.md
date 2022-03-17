# WiFi RunTime OS for ESP01 Modules

It is an application that aims to use the internet connection features of Wifux ESP01 module easily over other boards.

## How To Use
Codes can be loaded into an ESP01 module with Micropython loaded with GoozCLI or other tools. Afterwards, the module's UART pins must be connected to the device to exchange data.
### Connection to Internet
The following message should be sent to the ESP01 module
```shell
wifi connect --name [ssid] --password [password]
```
### HTTP Methods
```shell
curl get --url [URL]
```
