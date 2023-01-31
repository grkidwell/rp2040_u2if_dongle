
import os

os.environ["BLINKA_U2IF"]="1"

import board


from circuitpython_adapter import not_SMBus as SMBus

i2c_bus = SMBus(1)

def is_string(var):
    return type(var) == str

def dec2bytearray(dec):
    if is_string(dec):
        dec = int(dec,16)
    return [byte for byte in list(dec.to_bytes(2,byteorder='little'))]

def hex2bytearray(hex16):
    return dec2bytearray(int(hex16,16))

def bytearray2hex16(byte_array):
    hexbyte16 = ''
    for byte in reversed(byte_array):
        hexbyte16 += f"{int(hex(byte)[2:4],16):02x}"
    return '0x'+hexbyte16

def bytearray2dec(byte_array):
    hexbyte16=bytearray2hex16(byte_array)
    return int(hexbyte16,16)

