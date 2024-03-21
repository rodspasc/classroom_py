# Programação orientada a objetos.
# classes e objetos

class Veiculo:

    def __init__(self, fabricante, modelo):  # contrutor da classe veículo,  __ torna o atributo privado
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    def get_fabricamnte_modelo(self): # método para obter atributos privados do objeto veículo, 
        # desta forma (print) somente será possivel visualizar os atributos nada poderá ser feito com eles
        print(f'Modelo: {self.__modelo}, Fabricante {self.__fabricante}')  

    def get_num_registro(self):  # método para obter atributos privados do objeto veículo, 
        # desta forma (return) será possivel visualizar e usar os valores dos atributos em outras partes do progrma
        return self.__num_registro
    
    def set_num_registro(self, num_registro): # método para definir o número de registro do objeto veículo
        self.__num_registro = num_registro 
            
    def movimentar(self):  # método que define a ação de mavimento do objeto veículo
        print('\nSou um veículo e me desloco')


class Carro(Veiculo): # nova classe Carro que herda da veículo

    # método __init__ será herdado de veículo
    # método get e set será herdado de veículo

    def movimentar(self): # método que define a ação de movimento do objeto carro 'polimorfismo'
        print('Sou um carro e ando pelas ruas') 

class Motocicleta(Veiculo): # nova classe que herda de veículo

    # método __init__ será herdado de veículo
    # método get e set será herdado de veículo

    def movimentar(self): # método que define a ação de movimento do objeto motocicleta 'polimorfismo'
        print('Sou uma moto, corro muito, cuidado para ser morto só falta o r no meio!!!') 

class Aviao(Veiculo): # nova classe que herda de veículo

    def __init__(self, fabricante, modelo, categoria):  # define um atributo exclusivo do objeto avião 
        self.__categoria = categoria
        super().__init__(fabricante, modelo)  # herda da super classe veículo os demais atributos   

    # método get e set, para alguns atributos, será herdado de veículo
             
    def get_categoria(self):  # método para obter atributos privados do objeto avião, 
        # desta forma (return) será possivel visualizar e usar os valores dos atributos em outras partes do progrma
        return self.__categoria

    def movimentar(self): # método que define a ação de movimento do objeto avião 'polimorfismo'
        print('Eu sou um avião e voo alto!')

    
if __name__ == '__main__':
    
    meu_veiculo = Veiculo('Gurgel', "Br")
    meu_carro = Carro('GM','Celta')
    minha_moto = Motocicleta('Honda', 'CG')
    meu_aviao = Aviao('747','Boing','Comercial')    

    meu_veiculo.set_num_registro(123456)
    meu_veiculo.get_fabricamnte_modelo() 
    print(f'\nO numero de registro deste veículo é: {meu_veiculo.get_num_registro()}')
    meu_veiculo.movimentar()
   



