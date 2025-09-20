nome = input('Qual é o seu nome? ')

print('Olá,', nome)

idade = int(input('Quantos anos você tem? '))

alt = float(input('Qual a sua altura? '))

peso = float(input('E qual é o seu peso(em kg)? '))


imc = peso / (alt ** 2)


if imc == 0:
    print('Digite um peso e uma altura válida.')
    

elif imc >= 30:
    print('Cuidado, seu indíce de massa corporal indica que está com obesidade')
    
elif imc >= 25 and imc <= 29.99:
    print('Seu índice de massa corporal indica que você está com sobrepeso')
    
elif imc >= 18.5 and imc <=24.99:
    print('Seu índice de massa corporal indica que você está no peso ideal')
    
elif imc < 18.5:
    print('Seu índice de massa corporal indica que você está abaixo do peso')