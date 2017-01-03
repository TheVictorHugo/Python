class ValorRetidoErro(Exception):
        pass

        def main():
                lista = []
                for i in range(3):
                        while True:
                                try:
                                        num = int(input('Digite um numero: '))
                                        break
                                except ValueError:
                                        print('Digite apenas numeros')
                        if num not in lista:
                                lista.append(num)
                        else:
                                raise ValorRetidoErro
main()
