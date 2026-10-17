#Sites mais usados:
    # flask (criar site> mais usado)
    # django (criar site> mais usado)
    # fast api (criar api)
    # tornado (criar site> menos usado)
    # flet (criar site/ app/programa de computador> novo )
#{chaves} sao usadas para textos dinamicos, como conversas
#[couchetes] lista de coisas


#Titulo:mandyzap
#Passo 1-> Botão: iniciar chat
    #Popup/modal/alerta (um def vai sempre abrir um desses)
        #Titulo: bam vindo ao mandyzap
        #Campo de texto:ESCREVA seu nome aqui
        # Passo 2-> Botão : entrar chat
            #Sumir com o titulo e botão iniciar
            #Fechar popup
            #Criarchat
            #Embaixo do chat:
                #Campo de texto
                #Botão enviar
                    #Vai aparecer a mensagem no chat com nome de usuario
                    #Amanda: "oi gente!"


#CRIAR SITE

#Importar o flet
import flet as ft

#criar função principal do sistema
def main(pagina):
    #se quiser muddar a cor da pagina:pesquisar por "flet python", ir no site, doc,control, layout.
    #pagina.bgcolor
    #criar alguma coisa
    #criar titulo
    titulo = ft.Text('Mandyzap', size= 25, italic=True, color= ft.colors.ORANGE_500) 

    chat= ft.Column()
    titulo_janela = ft.Text('Bem Vindo ao chat da mais Linda')
    campo_nome_usuario = ft.TextField(label='escreva seu nome')

    #socket = tunel de comunicação
    #CRIAR TUNEL EM duas ETAPAS: ETAPA 1, FUNÇÃO DO TUNEL
    def mensagem_tunel(mensagens):
        chat.controls.append(ft.Text(mensagens))
        pagina.update()

        #CRIA O TUNEL: ETAPA 2
        #pubsub chama o "mensagem_tunel"
    pagina.pubsub.subscribe(mensagem_tunel)
        
       

    # passar todos os botões por lado de fora

    

    def enviar_mensagem(evento):
        #enviar mensagem e limpar o campo de msg :
            textinho = f'{campo_nome_usuario.value}: {texto_mensagem.value}'
            ########## não add ele ou duplica a msg :chat.controls.append(ft.Text(textinho))

            #enviar msg
            pagina.pubsub.send_all(textinho)
            #limpar o campo para escrever novamente;
            texto_mensagem.value = ""
            pagina.update()

        #para adicionar uma imagem colocar:
        #arquivo = ft.FilePicker()

    texto_mensagem = ft.TextField(label='digite sua mensagem', on_submit= enviar_mensagem)
    botao_enviarmsg = ft.Button("enviar mensagem", on_click= enviar_mensagem)
         #on_submit= enter
    
    # Passo 2-> Botão : entrar chat

    #organizar em linha para que um fique ao lado do outro, e não em cima e em baixo:
    linha_mensagem = ft.Row ([texto_mensagem, botao_enviarmsg])
    def abrir_conversa(evento):
        #tirar o titulo ao abrir isso
        pagina.remove(titulo)
        #tirar o botao iniciar
        pagina.remove(botao_iniciar)
        #fechar o popup
        janela.open= False # janela é o unico que é removido de forma diferente
        #criar o chat
        pagina.add(chat)

        #criar o campo de texto de enviar a msg
            #pagina.add (texto_mensagem)
        #criar o botão de enviar msg
            #pagina.add (botao_enviarmsg)
        pagina.add(linha_mensagem)

        #escrever "usuario entrou no chat":
        #f = formatar de tal forma
        texto_entrou_chat = (f'{campo_nome_usuario.value} entrou no chat')
        #append= adicionar a lista
        # nao vai mais adicionar na tela, entao tem q mandar isso la pra cima :chat.controls.append(ft.Text(texto_entrou_chat))
        pagina.pubsub.send_all(texto_entrou_chat)
        pagina.update()

    botao_entrar = ft.Button("entrar no chat", on_click = abrir_conversa)

    #SE QUISER MUDAR O FORMATO DA CAXA DE TEXTO:  pesquisar por "flet python", ir no site, doc,control, alertdialog. 
    janela = ft.AlertDialog(
        title = titulo_janela,
        content = campo_nome_usuario,
        actions =[botao_entrar]
    )
    #pode ser 1 botao ou varios dentro do couchete[]

    def abrir_popup(evento):
        pagina.dialog = janela 
        #toda pagina tem um unico "dialog"
        janela.open = True
        #toda vez que mudar o site viualmente tem que atualziar: pagina.update()
        pagina.update()
        
    #Passo 1-> Botão: iniciar chat
    botao_iniciar= ft.Button('Iniciar Chat', on_click=abrir_popup)

    #colocar coisa na pagina
    #adicionar titulo
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    

#executar o sistema
    #ft.WEB_BROWSER(transforma em site na web)
ft.app(main, view= ft.WEB_BROWSER)

