print ( "Bem vindo a Calculadora de IMC" )

pergunta_nome  =  input ( "Qual é o seu nome? " )
nome  = ( "Olá" , pergunta_nome )
idade  =  input ( f"Qual sua idade? " )
peso  =  float ( input ( "Qual seu peso (em KG)? " ))
altura  =  float ( input ( "Qual sua altura (em metros e usando ponto)? " ))

print ( "Vamos calcular seu IMC" )

imc  = ( peso  / ( altura  *  altura ))

print ( pergunta_nome , ' seu IMC é {:.2f}: '.format(imc) ) #( f"seu IMC é: { imc :.2f } " )

if  imc  <  16 :
        print ( "Seu estado é de Magreza grave \n Procure um médico ou nutricionista." )
elif  imc  <  17 :
        print ( "Seu estado é de Magreza moderado \n Precisa rever sua alimentação." )
elif  imc  <  18.5 :
        print ( "Seu estado é de Magreza leve \n Precisa rever sua alimentação." )
elif  imc  <  25 :
        print ( "Você é Saudável. \n Parabéns!" )
elif  imc  <  30 :
        print ( "Seu estado é de Sobrepeso \n Precisa rever sua alimentação." )
elif  imc  <  35 :
        print ( "Seu estado é de Obesidade Grau \n Procure um médico ou nutricionista." )
elif  imc  <  40 :
        print ( "Seu estado é de Obesidade Grau II (severa) \n Procure um médico ou nutricionista." )
else:
        print ( "Seu estado é de Obesidade Grau III (mórbida) \n Procure um médico ou nutricionista." )
