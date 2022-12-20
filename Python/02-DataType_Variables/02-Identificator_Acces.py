# Library ctypes to access to the identificator content
import ctypes

print('\nIdentificator of the object: number 42 <id(42)>')
# Function id() returns the object identificator
print(id(42))

# In this concret case returns 140645844731408
# With ctypes we can access to the content on that memory identificator (pointer)
var = ctypes.cast(id(42), ctypes.py_object).value
print(var)
print(id(42))





