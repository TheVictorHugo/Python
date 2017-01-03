class Meu_Objeto:
    def __init__(pessoa):
        pessoa.nome = 'Pedro'
        pessoa.idade = 3
        print('Chamando o construtor')
    def imprime(pessoa):
        print('Olá meu nome é %s e eu tenho %d' %(pessoa.nome, pessoa.idade))
Pedro = Meu_Objeto()
