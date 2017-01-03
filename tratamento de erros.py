try:
    x = int(input('Digite um numero: '))
except:
    print('Deu erro, insira apenas numeros')
    x = 0
    
finally:
    print('O valor digitado é: ', x)
    
