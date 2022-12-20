import math

def hello_world():
    print('Hello world!')

def calculate_square(num):
    return math.sqrt(num)

def main_function(length):
    hello_world()
    print([x * 2 for x in range(length)])
    while True:
        num = float(input('Introduce a number: '))
        res = calculate_square(num)
        print(f'The square of {num} is {res}')

if __name__ == '__main__':
    main_function(10)