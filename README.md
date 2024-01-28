# arduino-icsp
Arduino sketch that implements a programmer for PIC devices that use the low
voltage In Circuit Serial Programming protocol.

## Usage
### Flash sketch on Arduino 
First, flash the `arduino_icsp.ino` sketch to an Arduino. This was tested with
a nano, but should work on most boards.

### Connect Arduino to PIC
Connect the Arduino to the PIC chip you would like to program. This requires 3
connections for ICSP: a bidirectional data line (DAT), a clock line (CLK), and
a reset line (MCLR). _Remember to also connect power!_

| Pin | ICSP |
|:---:|:----:|
| 10  | MCLR |
| 11  | CLK  |
| 12  | DAT  |

### Helper Programs
The arduino-icsp programmer takes a simple ascii based command set, so
theoretically you could interface manually using something like `screen`.

The recommend program to upload hex files to a PIC using the arduino-icsp
programmer is [picchick](https://github.com/Rex--/picchick).
This program supports arduino-icsp with the `-c arduino-icsp` command line option.

Additionally a python script `icsp.py` is provided that implements the basic
command set as command line arguments. This script requires `pyserial` to be
installed in order to communicate with serial devices.

## Copying
Copyright (c) 2024 Rex McKinnon \
This software is provided for free under the permissive University of
Illinios/NCSA Open Source License. Check out the LICENSE file for full details.
