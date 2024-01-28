import serial
import time
import sys


def usage():
    n = sys.argv[0]
    print(n+' r[ead] <address> [length]')
    print(n+' w[rite] <address> <data> [data...]')
    print(n+' e[rase] <address>')

def start():
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=5)
    print('Waiting for arduino bootloader...', end=' ', flush=True)
    time.sleep(2)
    print('done')

    ser.write(b's') # Start programming mode
    if ser.read() == b'K':
        print('Entered programming mode')
    else:
        print('ERROR: Failed to enter programming mode!')
        return None
    
    return ser



def write(ser):
    if len(sys.argv) < 4:
        print('ERROR: Invalid arguments')
        usage()
        return
    
    addr = int(sys.argv[2], 0)
    numWords = len(sys.argv) - 3
    
    ser.write(b'w') # Write command
    ser.write(addr.to_bytes(2, 'big')) # Address
    ser.write(numWords.to_bytes(2, 'big')) # num of words
    # words = []
    for word in sys.argv[3:]:
        # words.push(int(word, 0).to_bytes(2, 'big'))
        ser.write(int(word, 0).to_bytes(2, 'big')) # Write data
        print(word)

    resp = ser.read()
    if resp != b'K':
        print('ERROR: Failed to write: ' + resp)


def read(ser):
    if len(sys.argv) == 3:
        addr = int(sys.argv[2], 0)
        numWords = 1
    elif len(sys.argv) == 4:
        addr = int(sys.argv[2], 0)
        numWords = int(sys.argv[3], 0)
    else:
        print('ERROR: Invalid arguments')
        usage()
        return

    ser.write(b'r') # Read command
    ser.write(addr.to_bytes(2, 'big')) # Address
    ser.write(numWords.to_bytes(2, 'big')) # num of words
    resp = ser.read(numWords * 2) # Read words * 2 bytes
    
    print('Response:', resp.hex(' ', -2))
    # print('Response:', resp)

def erase(ser):
    pass

def exit(ser):
    ser.write(b'x') # Exit programming modes
    ser.close() # Close serial port

COMMANDS = {
    'r': read,
    'w': write,
    'e': erase,
}

cmd = sys.argv[1]

if cmd in COMMANDS:
    ser = start()
    if ser is not None:
        COMMANDS[cmd](ser)
        exit(ser)
elif cmd[0] in COMMANDS:
    ser = start()
    if ser is not None:
        COMMANDS[cmd[0]](ser)
        exit(ser)
else:
    print('Unknown command: \'' + cmd + '\'')
    usage()
