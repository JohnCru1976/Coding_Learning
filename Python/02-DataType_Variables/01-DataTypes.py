print('\n**************** PYTHON DATA TYPES ****************')
print('       **********************************          ')
print('**************** NUMERICAL ****************')

intNum = 1_999
print('1_999 => ' + str(intNum) + ' ' + str(type(intNum)) + " - Mutable: NO")

floatNum = 5.7e8
print('5.7e8 => ' + str(floatNum) + ' ' + str(type(floatNum)) + " - Mutable: NO")

complexNum = 2 + 5j
print('2 + 5j => ' + str(complexNum) + ' ' + str(type(complexNum)) + " - Mutable: NO")

print('\n**************** SEQUENCES ****************')

listSeq = [3.14, 2, False, 'c']
print('[3.14, 2, False, "c"] => ' + str(listSeq) + ' ' + str(type(listSeq)) + " - Mutable: YES")

tupleSeq = (3, 4, True)
print('(3, 4, True) => ' + str(tupleSeq) + ' ' + str(type(tupleSeq)) + " - Mutable: NO")

rangeSeq = range(5)
print('range(5) => ' + str(rangeSeq) + ' ' + str(type(rangeSeq)) + " - Mutable: NO")

print('\n**************** TEXT SEQUENCES ****************')

strSeq = '''tecla ''' + """gato """ + 'casa ' + "color"
print('\'\'\'tecla \'\'\' + """gato """ + \'casa \' + "color" => ' + str(strSeq) + ' ' + str(type(strSeq)) + " - Mutable: NO")

print('\n**************** BINARY SEQUENCES ****************')

bytesSeq = b'coche'
print('b\'coche\' => ' + str(bytesSeq) + ' ' + str(type(bytesSeq)) + " - Mutable: NO")

bytearraySeq = bytearray(b'coche')
print('bytearray(b\'coche\') => ' + str(bytearraySeq) + ' ' + str(type(bytearraySeq)) + " - Mutable: YES")

print('\n**************** SETS ****************')

setSET = set([3, True, 2]), {4, False, 12}
print('set([3, True, 2]), {4, False, 12} => ' + str(setSET) + ' ' + str(type(setSET)) + " - Mutable: YES")

frozensetSET = frozenset([2, 'hola', True, 3])
print('frozenset([2, \'hola\', True, 3]) => ' + str(frozensetSET) + ' ' + str(type(frozensetSET)) + " - Mutable: NO")

print('\n**************** MAPS ****************')

dictMAP = {'x': 1, 'y': 2}
print('{\'x\': 1, \'y\': 2} => ' + str(dictMAP) + ' ' + str(type(dictMAP)) + " - Mutable: YES")
dictMAP = dict(x=90,y=20)
print('dict(x=90,y=20) => ' + str(dictMAP) + ' ' + str(type(dictMAP)) + " - Mutable: YES")


