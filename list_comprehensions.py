def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2) #Se hace una lista de los numeros enteros elevado al cuadrado que no son divisibles por 3#

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    multiplos_36 = [i for i in range (1, 100000) if i % 36 ==0]

    multiplos_36_2 = [i for i in range (1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    if multiplos_36 == multiplos_36_2:
        print('Son iguales')
    else:
        print('no son iguales')       
    print(squares)


if __name__  == '__main__':
    run()