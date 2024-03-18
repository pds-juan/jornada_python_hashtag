# Título: MeuZap

# Botão de iniciar chat
    # Clicou no botão:
        # popup / modal
        # Subtítulo: Bem-vindo ao MeuZap
        # Campo: escreva seu nome
        # Botão: entrar no chat

# Chat
# embaixo do chat
    # Campo: digite sua mensagem
    # Botão: enviar

# flet -> framework do Python
# pip install flet

import flet as ft

def main(pagina): # criar a função principal
    texto = ft.Text("MeuZap", size=24, italic=False, color=ft.colors.BLUE_300)

    chat = ft.Column()

    # entrar_chat está aqui para conseguir usar on_submit em nome_usuario
    def entrar_chat(evento):
        # texto_entrada = ft.Text(f"{nome_usuario.value} entrou no chat")
        # chat.controls.append(texto_entrada)
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        # criar o chat
        pagina.add(chat)
        # fechar o popup
        popup.open = False
        # tirar o botão de entrar no chat
        pagina.remove(botao_iniciar)
        # tirar o título MeuZap
        # pagina.remove(texto)
        # colocar o campo de digitar mensagem
        # criar o botão de enviar
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        pagina.update()

    nome_usuario = ft.TextField(label="Digite o seu nome", on_submit=entrar_chat)

    def enviar_mensagem_tunel(mensagem):
        # adicionar a mensagem no chat de todos
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", size=12, italic=True, color=ft.colors.RED_500))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})
        # adicionar a mensagem no chat
        # texto_mensagem = ft.Text(campo_mensagem.value)
        # chat.controls.append(texto_mensagem)
        # limpar o campo de mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    # antes entrar_chat estava aqui

    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title=ft.Text("Bem-vindo!"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER) # criar o app chamando a função principal