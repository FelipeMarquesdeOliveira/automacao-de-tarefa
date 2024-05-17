# IMPORTANDO AS BIBLIOTECAS NECESSÁRIAS
import pyautogui
import time

# CRIANDO A FUNÇÃO PARA CLICAR NAS COORDENADAS
def clicar_em_coordenadas(coordenadas):
    for coord in coordenadas:
        if coord is not None:
            pyautogui.click(coord)
            time.sleep(1)

# CRIANDO A FUNÇÃO PARA LOCALIZAR OS BOTÕES COM TEMPO LIMITE
# CONFIDENCE: DEFINE O NÍVEL DE CONFIANÇA PARA A CORRESPONDÊNCIA DE IMAGEM DURANTE A LOCALIZAÇÃO DE UM BOTÃO NA TELA
def localizar_botao_com_tempo_limite(imagem_botao, tempo_limite=3, confidence=0.8):
    start_time = time.time()
    while time.time() - start_time < tempo_limite:
        botao_pos = pyautogui.locateCenterOnScreen(imagem_botao, confidence=confidence)
        if botao_pos is not None:
            return botao_pos
        time.sleep(0.1)  
    print(f"Botão {imagem_botao} não encontrado dentro do tempo limite.")
    return None

# DEFININDO COORDENADAS DOS BOTÕES 1, 2, 5

primeiroClick = (1879, 649)
segundoClick = (1752, 764)
quintoClick = (1050, 879)

# DEFININDO IMAGENS DOS BOTÕES 3, 4, 6

imagem_botao_3 = 'botao3.png'
imagem_botao_4 = 'botao4.png'
imagem_botao_6 = 'botao6.png'

# DEFININDO O INTERVALO DE CLIQUES

intervalo = 4

while True:
    # EXECUTANDO A FUNÇÃO clicar_em_coordenadas E CLICANDO NOS BOTÕES 1 E 2
    clicar_em_coordenadas([primeiroClick, segundoClick])
    # CRIANDO UMA VARIÁVEL PARA ARMAZENAR A LOCALIZAÇÃO DO BOTÃO 3 
    terceiroClick = localizar_botao_com_tempo_limite(imagem_botao_3, tempo_limite=3)
    
    if terceiroClick is not None:
        # EXECUTANDO A FUNÇÃO clicar_em_coordenadas E CLICANDO NO BOTÃO 3 - botao3.png
        clicar_em_coordenadas([terceiroClick])
        # CRIANDO UMA VARIÁVEL PARA ARMAZENAR A LOCALIZAÇÃO DO BOTÃO 4
        quartoClick = pyautogui.locateCenterOnScreen(imagem_botao_4, confidence=0.8)
        if quartoClick is not None:
            # EXECUTANDO A FUNÇÃO clicar_em_coordenadas E CLICANDO NO BOTÃO 4 - botao4.png
            clicar_em_coordenadas([quartoClick])
            # EXECUTANDO A FUNÇÃO clicar_em_coordenadas E CLICANDO NO BOTÃO 5
            clicar_em_coordenadas([quintoClick])
            # PAUSA NO CÓDIGO DE 0.5s
            time.sleep(0.5)
            # CLICANDO NO ATALHO ctrl + v PARA COLAR UM TEXTO
            pyautogui.hotkey('ctrl', 'v')
            # CRIANDO UMA VARIÁVEL PARA ARMAZENAR A LOCALIZAÇÃO DO BOTÃO 6
            sextoClick = pyautogui.locateCenterOnScreen(imagem_botao_6, confidence=0.8)
            if sextoClick is not None:
                # EXECUTANDO A FUNÇÃO clicar_em_coordenadas E CLICANDO NO BOTÃO 6 - botao6.png
                clicar_em_coordenadas([sextoClick])
                # DANDO UM INTERVALO DE 4 SEGUNDOS PARA QUE A PÁGINA POSSA SER RECARREGADA
                time.sleep(intervalo)
