n1 = int(input('Digite um número: '))

if n1 <= 0:
    print('Número inválidop! ')
else:
    contador = 1
    print(f'Tabuada de {n1}')

    while contador <= 10:
        resultado = contador * n1
        print(f'{n1} x {contador} = {resultado}')
        contador += 1