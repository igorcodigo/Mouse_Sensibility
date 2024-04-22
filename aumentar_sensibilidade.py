import time
import pyautogui

# Variáveis para armazenar a posição anterior e a posição atual
pos_anterior = None
tempo_espera = 0.025  # Intervalo de 0,1 segundos

# Loop para verificar a posição do mouse a cada 0,1 segundos
while True:
    # Obtém a posição atual do mouse
    pos_atual = pyautogui.position()

    # Se não houver uma posição anterior, inicialize-a como a posição atual
    if pos_anterior is None:
        pos_anterior = pos_atual

    # Calcula a diferença entre a posição anterior e a posição atual
    diff_x = pos_atual.x - pos_anterior.x 
    diff_y = pos_atual.y - pos_anterior.y

    # Exibe as informações no console
    print(f"Posição anterior: {pos_anterior}")
    print(f"Posição atual: {pos_atual}")
    print(f"Diferença em X: {diff_x}, Diferença em Y: {diff_y}")
    print("-" * 20)

    # Calcula a nova posição com base na diferença 
    if diff_x < 0: nova_posicao_x = pos_atual.x + diff_x*10
    else: nova_posicao_x = pos_atual.x + diff_x*4

    nova_posicao_y = pos_atual.y + diff_y*4

    # Move o mouse para a nova posição
    pyautogui.moveTo(nova_posicao_x, nova_posicao_y, duration=0)
    pos_atual = pyautogui.position()
    # Atualiza a posição anterior para a posição atual
    pos_anterior = pos_atual

    # Espera por 0,1 segundos antes de verificar novamente
    time.sleep(tempo_espera)
