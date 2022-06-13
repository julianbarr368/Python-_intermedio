def divisor(num):
    divisors = []
    try: 
        if num < 0 :
            raise ValueError('Ingrese SOLO numeros positivos.... Gracias')
        for i in range (1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return('Intenta de nuevo')


def run():
    try:
        num = int(input('Ingrese un numero: '))
        print(divisor(num))
        print('Termino mi programa')
    except ValueError:
        print('Debes ingresar un numero...')
       


if __name__ == '__main__':
    run()