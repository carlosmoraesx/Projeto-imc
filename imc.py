altura = float(input('qual é a sua altura:'))
peso = float(input('Qual seu peso:'))

IMC = peso/ (altura/100)**2

print(IMC)

if IMC < 18.5:
    print(f'Seu IMC é de {IMC}, e é clasificado como magreza')

elif IMC >= 18.5 and IMC < 24.9:
     print(f'Seu IMC é de {IMC}, e é clasificado como normal')
    
elif IMC >= 25 and IMC < 29.9:
     print(f'Seu IMC é de {IMC}, e é clasificado como sobrepeso')

elif IMC >= 30 and IMC < 39.9:
     print(f'Seu IMC é de {IMC}, e é classificado como Obesidade')

else:
     print("Reduza a alimentação, já esta em um grau avançado de obesidade")

     
#Menor que 18,5	Magreza
#18,5 a 24,9	Normal
#25 a 29,9	Sobrepeso
#30 a 34,9	Obesidade grau I
#35 a 39,9	Obesidade grau II
#Maior que 40	Obesidade grau III