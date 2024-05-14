import pyautogui
import time

# DEFINIÇÃO DA FUNÇÃO PARA CLICAR EM UMA LISTA DE COORDENADAS
def clicar_em_coordenadas(coordenadas):
    for coord in coordenadas:
        pyautogui.click(coord)
        time.sleep(4)  

# COORDENADAS DE CLIQUES
primeiroClick = (1879, 649)
segundoClick = (1752, 764)
terceiroClick = (381, 711)
quartoClick = (382, 834)
quintoClick = (1050, 879)
sextoClick = (1832, 932)

# LISTA DE TODAS AS COORDENADAS DE CLIQUE
todos_cliques = [primeiroClick, segundoClick, terceiroClick, quartoClick, quintoClick, sextoClick]

# INTERVALO ENTRE CLIQUES
intervalo = 4

# LOOP PRINCIPAL
while True:
    clicar_em_coordenadas(todos_cliques[:-1]) 
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(sextoClick)
    time.sleep(intervalo)
