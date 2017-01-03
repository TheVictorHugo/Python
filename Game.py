'''
class Meu_Objeto:
    def __init__(pessoa, nome, idade):
        pessoa.nome = nome
        pessoa.idade = idade
        print('Chamando o construtor')
    def imprime(pessoa):
        print('Olá meu nome é %s e eu tenho %d' %(pessoa.nome, pessoa.idade))

Pedro = Meu_Objeto('Victor', 24)
Victor.imprime()
'''
Pessoa = {'Nome': 'Victor', 'Profissao': 'Programagor', 'idade': 24}


#Pessoa ['Nome'] = 'Hugo'
print(Pessoa ['Profissao'])

class Pessoa:
    pass
Victor = Pessoa()

Victor.nome = 'Victor'
Victor.emprego = 'Programador'
Victor.idade = 24


print(Victor.__dict__)

