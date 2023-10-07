''' RECURSION
This code is an exercise
'''

def decimal_binary(number):
    '''The parameter must be an integer, if it isn't the function returns -1'''
    try:
        x = int(number)
    except ValueError:
        return "-1"

    if x == 0:
        return "0"
    if x == 1:
        return "1"
    return decimal_binary(x // 2) + str(x % 2)

def binary_decimal(number):
    '''The number must be an string with 0's and 1's'''
    lista = list(str(number))
    if not lista:
        return 0
    x = int(lista.pop(0))
    y = len(lista)
    return (x * (2 ** y)) + binary_decimal("".join(lista))

# Test decimal to binary
i = 5
print(str(i) + " - " + decimal_binary(i))
# Test output binary to decimal
i = str(decimal_binary(i))
print(str(i) + " - " + str(binary_decimal(i)))


