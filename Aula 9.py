class Animal:
    def __init__(anim, cor, genero, andar):
        anim.cor = cor
        anim.genero = genero
        anim.num_de_patas = andar
        
    #def falar(anim):
        #print('Olá sou um cachorro e sei falar')
        
    def andar(anim):
        print('Estou andando sobre %i patas' %(anim.num_de_patas))
        
    def amamentar(anim):
        if anim.genero.lower() [0] == 'm':
            print('Machos não amamentam')
            return
        print('amamentando mei finhote')

#Rex = Animal ('marron', 'masculino', 4)
#Rex.falar()
#Rex.andar()
#Rex.amamentar()

class Pessoa(Animal):
    def __init__ (anim, cor, genero, andar, cabelo):
        super(Pessoa, anim).__init__(cor, genero, andar)
        anim.cabelo = 'Castanho'

    def falar(anim):
        super(Pessoa, anim).falar()
        print('Olá sou um pessoa e sei falar')
        
Victor = Pessoa('branco', 'masculino', 2, 'castanho')
Victor.falar
