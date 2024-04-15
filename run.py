from main import Eagle

texto = '''
Mensagem Aviso OK
'''


if __name__=="__main__":
    app = Eagle(status='OK', mensagem=texto, cor_aparencia='light')
    app.run()
