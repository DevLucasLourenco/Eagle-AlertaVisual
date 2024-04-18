import customtkinter as ctk
from typing import Literal
from PIL import Image
from pathlib import Path

class Eagle:
    
    def __init__(self, *ctk_instancia:object, status:Literal['X',"OK"], mensagem:str,titulo_janela:str=None, cor_aparencia:Literal['light','dark']='light') -> None:
        # Objetos
        #------------------------------
        self.master = None
        self.ctk_instancia = ctk_instancia
        self.cor_aparencia = cor_aparencia
        self.mensagem = mensagem
        self.status = status.upper()
        self.titulo_janela = titulo_janela if not titulo_janela == None else status
        #------------------------------
        
        # Utilizações
        #------------------------------
        self.icone_imagens:dict = {
            'OK':r'imagens/OK.png',
            'X':r'imagens/X.png',
            }
        
        self.cor_botao = {
            'OK': (r'#27C870', r'#0BA752'),
            'X':(r'#C80C0C', r'#990000')
        }
        #------------------------------
        
        
        self.tamanho_janela = '550x250'
        self.posicao_janela = None
        
        
        
    def run(self):
        self.__config_GUI_inicializacao()
        FQ = FrameQuadro(self)
        FI = FrameInferior(self)
        
        self.master.mainloop()

    
    def __config_GUI_inicializacao(self):
        if not self.ctk_instancia:
            self.master = ctk.CTk() 
        else:
            self.master = self.ctk_instancia.CTkToplevel(self.master)

        self.master.title(self.titulo_janela)

        self.largura_total = self.master.winfo_screenwidth()
        self.altura_total = self.master.winfo_screenheight()  
        
        
        x = (self.largura_total - int(self.tamanho_janela.split('x')[0])) // 2
        y = ((self.altura_total - int(self.tamanho_janela.split('x')[1])) - 100) // 2
        self.posicao_janela = '+'.join([str(x),str(y)])
        
        ctk.set_appearance_mode(self.cor_aparencia)
        
        self.master.geometry(f'{self.tamanho_janela}+{self.posicao_janela}')
        self.master.resizable(False, False)



class FrameQuadro():
    
    def __init__(self, objeto) -> None:
        self.objeto_main = objeto
        self.run()
    
    
    def run(self):
        self.areaImagem()
        self.areaTexto()
        
        
    def areaImagem(self):
        imagem = Image.open(self.objeto_main.icone_imagens[self.objeto_main.status])
        self.campo_imagem = ctk.CTkLabel(self.objeto_main.master,text='', image=ctk.CTkImage(dark_image=imagem, light_image=imagem, size=(50,50)))
        self.campo_imagem.place(relx=0.05, rely=0.05)
    

    def areaTexto(self):
        texto = self.objeto_main.mensagem
        self.campo_mensagem = ctk.CTkLabel(self.objeto_main.master, text=texto, wraplength=400, justify='left')
        self.campo_mensagem.place(relx=0.2, rely=0.025)
        

    
class FrameInferior():
    
    def __init__(self, objeto) -> None:
        self.objeto_main = objeto
        self.run()
        
        
    def run(self):
        self.criar_frame()
        self.criar_botao()
        
    
    def criar_frame(self):
        self.frame = ctk.CTkFrame(self.objeto_main.master, width=100, height=80, border_color='#BFBFBF', border_width=2)
        self.frame.pack_propagate(False)
        self.frame.pack(fill='x', side='bottom')
    
    
    def criar_botao(self):
        botao_fechar = ctk.CTkButton(master=self.frame, text="Fechar", width=100, height=40, corner_radius=5, 
                                     command=self.objeto_main.master.destroy, font=('Robolo',16,'bold'), 
                                     fg_color=self.objeto_main.cor_botao[self.objeto_main.status][0],
                                     hover_color=self.objeto_main.cor_botao[self.objeto_main.status][1])
        botao_fechar.pack(side='right', padx=10)


class EaglePausado(Eagle):
    
    def __init__(self, *master: object, status: Literal['X'] | Literal['OK'], mensagem: str, cor_aparencia: Literal['light'] | Literal['dark'] = 'light') -> None:
        super().__init__(*master, status=status, mensagem=mensagem, cor_aparencia=cor_aparencia)
    
    
    