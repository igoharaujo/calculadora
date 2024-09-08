import math
from calculos.quadrado import AreaQuadrado
from calculos.retangulo import AreaRetangulo
from calculos.circulo import AreaCirculo
from calculos.cubo import VolumeCubo
from calculos.paralelepipedo import VolumeParalelepipedo
from calculos.cilindro import VolumeCilindro
from calculo import Calculadora

def interface_calculos():
    calculadora = Calculadora()

    while True:
        print("\nEscolha a operação:")
        print("1 - Calcular área do quadrado")
        print("2 - Calcular área do retângulo")
        print("3 - Calcular área do círculo")
        print("4 - Calcular volume do cubo")
        print("5 - Calcular volume do paralelepípedo")
        print("6 - Calcular volume do cilindro")
        print("0 - Sair")

        opcao = input("\nDigite o número da operação desejada: ")

        if opcao == '0':
            break
        elif opcao == '1':
            lado = float(input("Digite o valor do lado do quadrado: "))
            quadrado = AreaQuadrado(lado)
            area = calculadora.medir_area(quadrado)
            print(f"A área do quadrado é: {area}")
        elif opcao == '2':
            largura = float(input("Digite o valor da largura do retângulo: "))
            comprimento = float(input("Digite o valor do comprimento do retângulo: "))
            retangulo = AreaRetangulo(largura, comprimento)
            area = calculadora.medir_area(retangulo)
            margem = calculadora.medir_margem(retangulo)
            print(f"A área do retângulo é: {area}")
            print(f"A margem do retângulo é: {margem}")
        elif opcao == '3':
            raio = float(input("Digite o valor do raio do círculo: "))
            circulo = AreaCirculo(raio)
            area = calculadora.medir_area(circulo)
            margem = calculadora.medir_margem(circulo)
            print(f"A área do círculo é: {area}")
            print(f"A margem do círculo é: {margem}")
        elif opcao == '4':
            lado = float(input("Digite o valor do lado do cubo: "))
            cubo = VolumeCubo(lado)
            volume = calculadora.medir_volume(cubo)
            print(f"O volume do cubo é: {volume}")
        elif opcao == '5':
            comprimento = float(input("Digite o valor do comprimento do paralelepípedo: "))
            largura = float(input("Digite o valor da largura do paralelepípedo: "))
            altura = float(input("Digite o valor da altura do paralelepípedo: "))
            paralelepipedo = VolumeParalelepipedo(comprimento, largura, altura)
            volume = calculadora.medir_volume(paralelepipedo)
            print(f"O volume do paralelepípedo é: {volume}")
        elif opcao == '6':
            raio = float(input("Digite o valor do raio do cilindro: "))
            altura = float(input("Digite o valor da altura do cilindro: "))
            cilindro = VolumeCilindro(raio, altura)
            volume = calculadora.medir_volume(cilindro)
            print(f"O volume do cilindro é: {volume}")
        else:
            print("Essa opção não é possível. Escolha uma das opções válidas.")

interface_calculos()
