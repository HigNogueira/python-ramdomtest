Python 2.7.17 (v2.7.17:c2f86d86e6, Oct 19 2019, 20:49:36) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  
#Simulador de dado	   
	# Simular o uso de um dado, gerando um valor de 1 até 6	   
	import random	   
	import PySimpleGUI as sg	   
	
	   
	class SimuladorDeDado:	   
	    def __init__(self):	   
	        self.valor_minimo = 1	   
	        self.valor_maximo = 6	   
	        # Layout	   
	        self.layout = [	   
	            [sg.Text('Jogar o dado?')],	   
	            [sg.Button('sim'),sg.Button('Não')]	   
	        ]	   
	    	   
	    def Iniciar(self):	   
	        # criar uma janela	   
	        self.janela = sg.Window('Simulador de Dado',layout=self.layout)	   
	        # ler os valores da tela	   
	        self.eventos, self.valores = self.janela.Read()	   
	        # fazer alguma coisa com esses valores	   
	        try:	   
	            if self.eventos == 'sim' or self.eventos == 's':	   
	                self.GerarValorDoDado()	   
	            elif self.eventos == 'Não' or self.eventos == 'n':	   
	                print('Agrecemos a sua participação!')	   
	            else:	   
	                print('Favor digitar sim ou não')	   
	        except:	   
	            print('Ocorreu um erro ao receber sua resposta')	   
	    	   
	    def GerarValorDoDado(self):	   
	        print(random.randint(self.valor_minimo,self.valor_maximo))	   
	
	   
	simulador = SimuladorDeDado()	   
	simulador.Iniciar()	 



