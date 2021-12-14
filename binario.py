#int to binary
def int_binary(num):
    binary = bin(num)
    binary = binary.replace("0b", "")
    print(binary)
# binary to int
def binary_int(num):
    binary = str(num)
    entero = 0
    pot = len(binary)
    for i in binary:
        if i == '1':
            entero += pow(2, pot-1)
        pot -= 1
    print(entero)

def run():
    option = input('1: int to binary, 2: binary to int: ')
    if option == '1':
        while True:
            try:
                num = int(input('Enter a number between 0 and 255: '))
                if num < 0:
                    raise ValueError
                if num >= 256:
                    raise ValueError
                int_binary(num)
                print('Finish')
                break
            except ValueError:
                print('Enter a number between range')
    else:
        while True:
            try:
                num = int(input('ingrese un número entre el 0 y el 255: '))
                if num < 0:
                    raise ValueError
                binary_int(num)
                print('Finish')
                break
            except ValueError:
                print('Enter a number between range')
        

if __name__ == '__main__':
    run()
    