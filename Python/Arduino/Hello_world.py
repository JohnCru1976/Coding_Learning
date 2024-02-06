'''Test con arduino'''
import serial

arduino = serial.Serial('COM3', 9600)

rawString = arduino.readline().decode('ascii')

print(rawString)

arduino.close()
