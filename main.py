import pyautogui
import time

def clicar_em_coordenadas(coordenadas):
    for coord in coordenadas:
        if coord is not None:
            pyautogui.click(coord)
            time.sleep(1)  

def localizar_botao_com_tempo_limite(imagem_botao, tempo_limite=3, confidence=0.8):
    start_time = time.time()
    while time.time() - start_time < tempo_limite:
        botao_pos = pyautogui.locateCenterOnScreen(imagem_botao, confidence=confidence)
        if botao_pos is not None:
            return botao_pos
        time.sleep(0.1)
    return None

def mover_para_posicao_1_e_scroll():
    posicao1 = localizar_botao_com_tempo_limite('posicao1.png')
    if posicao1 is not None:
        pyautogui.moveTo(posicao1)
        pyautogui.scroll(-1000)

imagem_botao_2 = 'despachar.png'
imagem_botao_3 = 'selecione.png'
imagem_botao_4 = 'arquivar.png'
imagem_botao_5 = 'caixa_texto.png'
imagem_botao_6 = 'salvar_despacho.png'
seta_direita_funcional = 'seta_direita_funcional.png'
seta_direita_nao_funcional = 'seta_direita_nao_funcional.png'
imagens_procuradas = ['colisao.png', 'perda.png', 'estelionato.png']

while True:
    encontrou_imagem_procurada = False
    
    for imagem in imagens_procuradas:
        coordenada = pyautogui.locateCenterOnScreen(imagem, confidence=0.8)
        if coordenada is not None:
            clicar_em_coordenadas([(coordenada.x, 649)])
            encontrou_imagem_procurada = True
            break
    
    if encontrou_imagem_procurada:
        despacharClick = localizar_botao_com_tempo_limite(imagem_botao_2, tempo_limite=3)
        if despacharClick is not None:
            clicar_em_coordenadas([despacharClick])
            
            terceiroClick = localizar_botao_com_tempo_limite(imagem_botao_3, tempo_limite=3)
            if terceiroClick is not None:
                clicar_em_coordenadas([terceiroClick])
                
                quartoClick = pyautogui.locateCenterOnScreen(imagem_botao_4, confidence=0.8)
                if quartoClick is not None:
                    clicar_em_coordenadas([quartoClick])
                    
                    mover_para_posicao_1_e_scroll()
                    
                    quintoClick = localizar_botao_com_tempo_limite(imagem_botao_5, tempo_limite=3)
                    if quintoClick is not None:
                        clicar_em_coordenadas([quintoClick])
                        
                        time.sleep(0.5)
                        pyautogui.write("Ao arquivo")
                        
                        sextoClick = pyautogui.locateCenterOnScreen(imagem_botao_6, confidence=0.8)
                        
                        if sextoClick is not None:
                            clicar_em_coordenadas([sextoClick])
                            
                            time.sleep(2)
    else:
        seta_direita = localizar_botao_com_tempo_limite(seta_direita_funcional, tempo_limite=3)
        if seta_direita is not None:
            clicar_em_coordenadas([seta_direita])
        else:
            if pyautogui.locateOnScreen(seta_direita_nao_funcional, confidence=0.8) is not None:
                print("Não há mais páginas para verificar.")
                break
