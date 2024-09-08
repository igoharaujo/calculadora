import tkinter as tk
import math
from calculos.quadrado import AreaQuadrado
from calculos.retangulo import AreaRetangulo
from calculos.circulo import AreaCirculo
from calculos.cubo import VolumeCubo
from calculos.paralelepipedo import VolumeParalelepipedo
from calculos.cilindro import VolumeCilindro
from calculo import Calculadora

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Formas")

        self.calculadora = Calculadora()

        self.create_widgets()

    def create_widgets(self):
        # Menu de operações
        self.label_menu = tk.Label(self.root, text="Escolha a operação:")
        self.label_menu.grid(row=0, column=0, columnspan=2)

        self.button_quadrado = tk.Button(self.root, text="1 - Calcular área do quadrado", command=self.calcular_quadrado)
        self.button_quadrado.grid(row=1, column=0, columnspan=2)

        self.button_retangulo = tk.Button(self.root, text="2 - Calcular área do retângulo", command=self.calcular_retangulo)
        self.button_retangulo.grid(row=2, column=0, columnspan=2)

        self.button_circulo = tk.Button(self.root, text="3 - Calcular área do círculo", command=self.calcular_circulo)
        self.button_circulo.grid(row=3, column=0, columnspan=2)

        self.button_cubo = tk.Button(self.root, text="4 - Calcular volume do cubo", command=self.calcular_cubo)
        self.button_cubo.grid(row=4, column=0, columnspan=2)

        self.button_paralelepipedo = tk.Button(self.root, text="5 - Calcular volume do paralelepípedo", command=self.calcular_paralelepipedo)
        self.button_paralelepipedo.grid(row=5, column=0, columnspan=2)

        self.button_cilindro = tk.Button(self.root, text="6 - Calcular volume do cilindro", command=self.calcular_cilindro)
        self.button_cilindro.grid(row=6, column=0, columnspan=2)

        self.button_sair = tk.Button(self.root, text="0 - Sair", command=self.root.quit)
        self.button_sair.grid(row=7, column=0, columnspan=2)

        # Entrada de dados
        self.label_entrada = tk.Label(self.root, text="")
        self.label_entrada.grid(row=8, column=0, columnspan=2)

        self.entry_entrada = tk.Entry(self.root)
        self.entry_entrada.grid(row=9, column=0, columnspan=2)

        self.button_calcular = tk.Button(self.root, text="Calcular", command=self.calcular)
        self.button_calcular.grid(row=10, column=0, columnspan=2)

        # Resultado
        self.resultado = tk.Label(self.root, text="")
        self.resultado.grid(row=11, column=0, columnspan=2)

        self.operacao = None

    def calcular_quadrado(self):
        self.operacao = "quadrado"
        self.label_entrada.config(text="Digite o valor do lado do quadrado:")
        self.entry_entrada.delete(0, tk.END)

    def calcular_retangulo(self):
        self.operacao = "retangulo"
        self.label_entrada.config(text="Digite os valores da largura e do comprimento do retângulo (separados por espaço):")
        self.entry_entrada.delete(0, tk.END)

    def calcular_circulo(self):
        self.operacao = "circulo"
        self.label_entrada.config(text="Digite o valor do raio do círculo:")
        self.entry_entrada.delete(0, tk.END)

    def calcular_cubo(self):
        self.operacao = "cubo"
        self.label_entrada.config(text="Digite o valor do lado do cubo:")
        self.entry_entrada.delete(0, tk.END)

    def calcular_paralelepipedo(self):
        self.operacao = "paralelepipedo"
        self.label_entrada.config(text="Digite os valores do comprimento, largura e altura do paralelepípedo (separados por espaço):")
        self.entry_entrada.delete(0, tk.END)

    def calcular_cilindro(self):
        self.operacao = "cilindro"
        self.label_entrada.config(text="Digite os valores do raio e da altura do cilindro (separados por espaço):")
        self.entry_entrada.delete(0, tk.END)

    def calcular(self):
        valores = self.entry_entrada.get().split()
        if self.operacao == "quadrado":
            lado = float(valores[0])
            quadrado = AreaQuadrado(lado)
            area = self.calculadora.medir_area(quadrado)
            margem = self.calculadora.medir_margem(quadrado)
            self.resultado.config(text=f"Quadrado - Área: {area}, Margem: {margem}")
        elif self.operacao == "retangulo":
            largura = float(valores[0])
            comprimento = float(valores[1])
            retangulo = AreaRetangulo(largura, comprimento)
            area = self.calculadora.medir_area(retangulo)
            margem = self.calculadora.medir_margem(retangulo)
            self.resultado.config(text=f"Retângulo - Área: {area}, Margem: {margem}")
        elif self.operacao == "circulo":
            raio = float(valores[0])
            circulo = AreaCirculo(raio)
            area = self.calculadora.medir_area(circulo)
            margem = self.calculadora.medir_margem(circulo)
            self.resultado.config(text=f"Círculo - Área: {area}, Margem: {margem}")
        elif self.operacao == "cubo":
            lado = float(valores[0])
            cubo = VolumeCubo(lado)
            volume = self.calculadora.medir_volume(cubo)
            self.resultado.config(text=f"Cubo - Volume: {volume}")
        elif self.operacao == "paralelepipedo":
            comprimento = float(valores[0])
            largura = float(valores[1])
            altura = float(valores[2])
            paralelepipedo = VolumeParalelepipedo(comprimento, largura, altura)
            volume = self.calculadora.medir_volume(paralelepipedo)
            self.resultado.config(text=f"Paralelepípedo - Volume: {volume}")
        elif self.operacao == "cilindro":
            raio = float(valores[0])
            altura = float(valores[1])
            cilindro = VolumeCilindro(raio, altura)
            volume = self.calculadora.medir_volume(cilindro)
            self.resultado.config(text=f"Cilindro - Volume: {volume}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
