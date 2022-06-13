def divisor(num):
    divisors = []
   
    for i in range (1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors
    


def run():
    num = (input('Ingrese un numero: ')) # Paso solo el string por que lo voy a necesitar asi para la funcion isnumeric()
    assert num.isnumeric() and int(num) >0 , "Debes ingresar un numero positivo" 
    print(divisor(int(num)))
    print('Termino mi programa')
    
       


if __name__ == '__main__':
    run()