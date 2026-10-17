import flet as ft


def main (pagina):
    chat = ft.Column()
    titulo= ft.Text("amandazap")
    
    def mensagem_tunel (mensagens):
        chat.controls.append (ft.Text(mensagens))
        pagina.update()
    pagina.pubsub.subscribe(mensagem_tunel)
    
    
    def enviar_chat (evento):
        textinho= f'{campo_mensagem.value}:{campo_msg.value}'
        pagina.pubsub.send_all(textinho)
        campo_msg.value = ""
        pagina.update()
    
    
    botao_enviar= ft.Button("ENVIAR", on_click= enviar_chat)
    campo_msg= ft.TextField (label= "escreva sua mensagem")
    linha_msg= ft.Row([campo_msg, botao_enviar])
    
    def abrir_tunel (evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open= False
        
        pagina.add(chat)
        pagina.add(linha_msg)
        
        texto_entrouchat = f'{campo_mensagem.value} entrou no chat'
        pagina.pubsub.send_all(texto_entrouchat)
        pagina.update()
    
    titulo_janela= ft.Text ("digite seu nome")
    campo_mensagem= ft.TextField (label="preencha aqui")
    botao_dois= ft.Button("entrar", on_click= abrir_tunel)
    janela = ft.AlertDialog(title= titulo_janela , content= campo_mensagem, actions=[botao_dois])
    
    def abrir_popup(evento):
        pagina.dialog= janela
        janela.open =True
        pagina.update()
            
    botao_iniciar= ft.Button("entrar", on_click= abrir_popup)
    
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    
ft.app(main, view= ft.WEB_BROWSER)
    