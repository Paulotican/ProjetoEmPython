nota1 = float(input('primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
média = (nota1 + nota2) / 2

print('A media entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1, nota2, média))
#if media >= 5 and 7:
if 7 > média >= 5:
    print('aluno de RECUPARAÇãO. ')
elif média < 5:
    print('Aluno REPROVADO')
elif média >= 7:
    print('aluno APROVADO')
#else:
 #   print('aluno APROVADO')