# Numbers => int float complex

# Int  constructor - n base to base 10
binary='1101101'
print(int(binary, base=2)) # Returns 109
octal='67'
print(int(octal, base=8)) # Returns 55
hexad='1b'
print(int(hexad, base=16)) # Returns 27

# Functions bin, oct, hex
print(bin(109)) # Returns '0b1101101'
print(oct(55)) # Returns '0o67'
print(hex(27)) # Returns 0x1b