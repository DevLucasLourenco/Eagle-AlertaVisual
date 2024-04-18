from main import Eagle


texto = '''
Mensagem Aviso OK
'''


if __name__=="__main__":
    app = Eagle(status='ok', mensagem=texto,
                cor_aparencia='dark', titulo_janela = 'teste')
    app.run()
