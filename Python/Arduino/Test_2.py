import time, serial

arduino = serial.Serial("COM3", 9600)

time.sleep(2)

number = input("Introduce a number (0-9)")

arduino.write(bytes(number,'utf-8'))

arduino.close()
