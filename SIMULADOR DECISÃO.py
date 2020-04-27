Python 2.7.17 (v2.7.17:c2f86d86e6, Oct 19 2019, 20:49:36) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
# Projeto CHAVE 5 - Decida por mim - RANDOM PY3.6	   
	# Faça uma pergunta para o programa e ele terá que te dar uma resposta	   
	import random	   
	import PySimpleGUI as sg	   
	
	   
	class DecidaPorMim:	   
	    def __init__(self):	   
	        self.respostas = [	   
	            'Com certeza, você deve fazer isso!',	   
	            'Não sei, você se sabe',	   
	            'Não faz isso Não!',	   
	            'Acho que tá na hora certa!'	   
	        ]	   
	
	   
	    def Iniciar(self):	   
	        # Layout	   
	        layout = [	   
	            [sg.Text('Faça sua pergunta:')],	   
	            [sg.Input()],	   
	            [sg.Output(size=(50,10))],	   
	            [sg.Button('Decida por mim')]	   
	        ]	   
	        # criar a janela	   
	        self.janela = sg.Window('Decida por Mim!',layout=layout)	   
	        while True:	   
	            # Ler os valores	   
	            self.eventos, self.valores = self.janela.Read()	   
	            # Fazer algo com os valores	   
	            if self.eventos == 'Decida por mim':	   
	                print(random.choice(self.respostas))
	        
	    	   
	decida = DecidaPorMim()	   
	decida.Iniciar()	 


