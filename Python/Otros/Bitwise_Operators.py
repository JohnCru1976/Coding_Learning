## OPERAR CON BITS
'''
& (ampersand) - bitwise conjunction (AND);
| (bar) - bitwise disjunction (OR);
^ (caret) - bitwise exclusive or (XOR).

~ (tilde) - bitwise negation;

& requires exactly two 1s to provide 1 as the result;
| requires at least one 1 to provide 1 as the result;
^ requires exactly one 1 to provide 1 as the result.

We must use integers - not floats

Bitwise operators are stricter: they deal with every bit separately.
'''
x = 3 & 4  # 011 & 100 = 000
print(bin(x))
x = 3 | 4  # 011 | 100 = 111   -> 7
print(bin(x))
x = 5 ^ 4  # 101 ^ 100 = 001
print(bin(x))

x = 0b1111 # 1.- 0b1111 + 1 = 0b10000    2.- -0b10000
y = ~x 
print(bin(x), x, sep=" - ")
print(bin(y), y, sep=" - ") 
x = -0b1111 # 1.- -0b1111 + 1 = -0b1110   2.- 0b1110
y = ~x 
print(bin(x), x, sep=" - ")
print(bin(y), y, sep=" - ") 
x = 0b0
y = ~x 
print(bin(x), x, sep=" - ")
print(bin(y), y, sep=" - ") 

### USOS DE BITWISE
## AVERIGUAR EL CONTENIDO DE UN BIT EN CONCRETO
flag_register = 0x1234  # 0b0001001000110100
# Queremos averiguar el contenido del bit con índice 3 (4 desde la derecha)
resultado = flag_register & 0b0000000000001000 # Si el bit 3 es 0 el resultado será 0b0
print(bin(resultado))
resultado = flag_register & 0b0000000000000100 # Si el bit 2 es 1 el resultado será 0b100
print(bin(resultado))

## SHIFTING

var = 17   #-> 10001
var_right = var >> 1  ## Mueve (shift) el número un lugar a la derecha -> 1000 = 17 // 2 = 8
var_left = var << 2  ## Mueve (shift) el número dos lugares a la izquierd -> 1000100 = 17 * 2**2 = 68
print(var, var_left, var_right)
