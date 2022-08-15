## LizardBrain shell documentation

On HW2.0/2.5 boards, there is an Infineon TriCore MCU that Tesla calls
"LizardBrain". It handles CAN communication, power, and thermal management,
and critical low-power ADAS functions such as park assist and AEB. On 
unfused boards, a telnet shell is accessible on LB. To access it, point 
your telnet client towards 192.168.90.104, port 23.

### Shell commands:
```
Trying 192.168.90.104...
Connected to lb.
Escape character is '^]'.
gw> help
Available commands:
help / ?: help
stat: lwIP statistics.
aurix_res: reset aurix
teg_res: reset parker primary 1=recovery 0=normal
teg_gpio: set parker primary gpio state [port] [state]
tegb_res: reset parker backup 1=recovery 0=normal
tegb_gpio: set parker backup gpio state [port] [state]
serial: serial communications [ch] 3=backup 2=primary 1=debug 0=gps [timeout sec] 0=no timeout
version: aurix firmware version 6=appConfig 5=appCrc 4=appHash 3=bootConfig 2=bootCrc 1=bootHash
genealogy: module pedigree 4=pkgSN 3=pkgPN 2=brdSN 1=brdPN
exit: exit.
```
### Enabling kmsg output
To enable kernel log output over serial, execute the following for both
tegras. This will switch the serial port to one with kernel output. Refer to
ftdi-map.txt for information on the 4-channel USB serial chip.
```
teg_gpio 1 1
tegb_gpio 1 1
```

### Entering APX mode (equivalent to fastboot or QDL mode):
```
teg(b)_res 1
```
