nome = input('Qual o nome do aluno? ')
n1 = int(input('Qual a sua primeira nota? '))
n2 = int(input('Qual a sua segunda nota? '))
media = (n1 + n2) / 2
print(f'De acordo com o dados do aluno {nome}, a sua primeria nota é {n1} e a sua segunda nota é {n2} então sua média é {media}')

if media < 5:
    print('Infelizmente você está sendo reprovado até o momento')
else:
    print('Aprovado')