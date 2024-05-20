 # Formulário Automático com PyAutoGUI

Este script automatiza a interação com um formulário na web, clicando em botões e preenchendo campos com base em imagens pré-definidas. Ele utiliza a biblioteca `pyautogui` para realizar essas ações.

## Funcionalidades

1. Lê se as opções desejadas estão disponíveis e responde ao formulário.
2. Localiza botões na tela e interage com eles.
3. Move a página para garantir que os botões sejam visíveis.
4. Preenche campos de texto e envia dados automaticamente.

## Como Funciona

### Funções Principais

- **clicar_em_coordenadas(coordenadas)**: 
  - Recebe uma lista de coordenadas e clica em cada uma delas com um intervalo de 1 segundo.
  
- **localizar_botao_com_tempo_limite(imagem_botao, tempo_limite=3, confidence=0.8)**: 
  - Procura a imagem do botão na tela durante um período de até 3 segundos. Retorna a posição do botão se encontrado, caso contrário, retorna `None`.
  
- **mover_para_posicao_1_e_scroll()**: 
  - Move para uma posição específica na tela e realiza um scroll para baixo para garantir que o botão esteja visível.

### Loop Principal

- O script roda em um loop contínuo, procurando pelas imagens especificadas em `imagens_procuradas`.
- Quando uma imagem é encontrada, ele clica na posição correspondente e segue uma sequência de interações definidas.
- Se a seta direita funcional (`seta_direita_funcional`) for encontrada, o script continua a execução. Se a seta não funcional (`seta_direita_nao_funcional`) for encontrada, o script para, indicando que não há mais páginas para verificar.
