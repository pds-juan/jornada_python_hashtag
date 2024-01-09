# Passo a passo do projeto

# Passo 1: Entrar no sistema da empresa -> https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# alguns comandos do PyAutoGUI:
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.25 # dependendo da velocidade do PC/navegador/internet, aumentar o tempo do PAUSE e dos times

# abrir o navegador (no meu caso o Brave)
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(0.25)


# Passo 2: Fazer login

# selecionar o campo de email
pyautogui.click(x=685, y=451)

# escrever o email
pyautogui.write("juan02pires@gmail.com")

# passando pro próximo campo
pyautogui.press("tab")

# escrever a senha
pyautogui.write("senha")

# clique no botao de login
pyautogui.click(x=955, y=638)

time.sleep(0.25)


# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

try:
    tabela = pd.read_csv("Aula 01/produtos.csv")
except FileNotFoundError:
    print("Arquivo 'Aula 01/produtos.csv' não encontrado. Certifique-se de que o arquivo existe no caminho especificado.")
    exit()
# print(tabela)


# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo até o último item

for linha in tabela.index:

    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    
    # preencher o campo
    pyautogui.write(str(codigo))
    
    # passar para o proximo campo
    pyautogui.press("tab")
    
    # fazendo o mesmo processo para cada outro campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    # cadastra o produto (botao enviar)
    pyautogui.press("enter")
    
    # dar scroll tudo pra cima
    pyautogui.scroll(1000)