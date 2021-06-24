'''
04.252.011/0001-10

0   4   2   5   2   0   1   1   0   0   0   1   X   X
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2=  65  ##

Formula -> 11 -(65 % 11) = 1 (Se o digito for maior que 9 vai ser 0 o digito)
Primeiro digito = 1

0   4   2   5   2   0   1   1   0   0   0   1   1   x
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2=  67  ##

Formula -> 11 - (67 % 11) = 11 (Como o resultado é maior que 9, então  é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original = 04.252.011/0001-10
Valido

'''
while True:
    cnpj = input('Digite o seu CNPJ: ')

    if not cnpj.isnumeric() or len(cnpj) < 14:
        print('Digite um CNPJ valido')
        continue
    else:
        cnpj = list(cnpj)

    novo_cnpj = cnpj[0:4]
    novo_cnpj_2 = cnpj[4:]

    reverso = 5
    reverso2 = 9

    resultado1 = []
    for i in range(4):
        resultado1.append(int(novo_cnpj[i]) * reverso)
        reverso -= 1
    soma1 = sum(resultado1)

    resultado2 = []
    for j in range(8):
        resultado2.append(int(novo_cnpj_2[j]) * reverso2)
        reverso2 -= 1
    soma2 = sum(resultado2)

    resultado_soma = soma1 + soma2

    validar = 11 - (resultado_soma % 11)

    if validar < 9:
        primeiro_digito = 1
        novo_cnpj.extend(novo_cnpj_2)
        novo_cnpj.append(primeiro_digito)
        print(novo_cnpj)

    ###################################################################################
    #### segundo digito

    novo_cnpj_3 = novo_cnpj[0:5]
    novo_cnpj_4 = novo_cnpj[5:]

    reverso3 = 6
    reverso4 = 9

    resultado3 = []
    for y in range(5):
        resultado3.append(int(novo_cnpj_3[y]) * reverso3)
        reverso3 -= 1
    soma3 = sum(resultado3)

    resultado4 = []
    for x in range(8):
        resultado4.append(int(novo_cnpj_4[x]) * reverso4)
        reverso4 -= 1
    soma4 = sum(resultado4)

    resultado_soma2 = soma3 + soma4

    validar2 = 11 - (resultado_soma2 % 11)

    if validar2 < 9:
        segundo_digito = 0
        novo_cnpj.append(segundo_digito)

    novo_cnpj_validado = ''.join(str(c) for c in novo_cnpj)
    print(novo_cnpj_validado)

    if novo_cnpj_validado == cnpj:
        print('CNPJ Valido')
    else:
        print('CNPJ Invalido')