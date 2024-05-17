import pyautogui
import time

#Função para localizar um botão na tela com um limite de tempo
def localizar_botao_com_tempo_limite(imagem_botao, tempo_limite=3, confidence=0.8):
    start_time = time.time()
    while time.time() - start_time < tempo_limite:
        botao_pos = pyautogui.locateCenterOnScreen(imagem_botao, confidence=confidence)
        if botao_pos:
            return botao_pos
        time.sleep(0.1)  
    print(f"Botão {imagem_botao} não encontrado dentro do tempo limite.")
    return None

#Função para clicar em um botão com um limite de tempo
def clicar_botao_com_tempo_limite(imagem_botao, tempo_limite=3):
    botao_pos = localizar_botao_com_tempo_limite(imagem_botao, tempo_limite)
    if botao_pos:
        pyautogui.click(botao_pos)

#Função para clicar em um botão e escrever um texto
def clicar_e_escrever(botao_imagem, texto, tempo_limite=3, delay=0.5):
    clicar_botao_com_tempo_limite(botao_imagem, tempo_limite)
    time.sleep(delay)
    pyautogui.write(texto)

#Dicionário contendo as imagens dos botões
imagens_botoes = {
    "botao1": "botao1.png",
    "botao2": "botao2.png",
    "botao3": "botao3.png",
    "botao4": "botao4.png",
    "botao5": "botao5.png",
    "botao6": "botao6.png"
}

#Imagem que define a posição desejada
posicao_imagem = "posicao1.png"

#Loop principal
while True:
    #Clicando nos botões na sequência indicada
    for nome_botao in ["botao1", "botao2", "botao3", "botao4"]:
        clicar_botao_com_tempo_limite(imagens_botoes[nome_botao])
    
    #Movendo o mouse para a posição específica e realizando um scroll
    posicao = pyautogui.locateCenterOnScreen(posicao_imagem, confidence=0.8)
    if posicao:
        pyautogui.moveTo(posicao)
        pyautogui.scroll(-1000)
    
    #Clicando no botão 5 e escrevendo "Ao Arquivo"
    clicar_e_escrever(imagens_botoes["botao5"], "Ao Arquivo")
    
    #Clicando no botão 6
    clicar_botao_com_tempo_limite(imagens_botoes["botao6"])
    
    #Aguardando um intervalo de 2 segundos antes de recarregar a página
    time.sleep(2)
