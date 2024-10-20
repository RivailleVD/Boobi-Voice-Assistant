import pygame
import os
from random import choice


def Bip_aleatorio ():
    # Inicializa o mixer de som
    pygame.mixer.init()

    # Caminho para a pasta que contém os arquivos de áudio
    caminho_pasta = "/home/levs/Músicas/Bips/Bips aleatorios"

    # Obtém uma lista de todos os arquivos na pasta
    arquivos_audio = [f for f in os.listdir(caminho_pasta) if f.endswith('.mp3')]

    # Escolhe um arquivo aleatório
    arquivo_escolhido = choice(arquivos_audio)

    # Caminho completo para o arquivo de áudio escolhido
    caminho_arquivo = os.path.join(caminho_pasta, arquivo_escolhido)

    # Carrega o arquivo de áudio
    pygame.mixer.music.load(caminho_arquivo)

    # Reproduz o áudio
    pygame.mixer.music.play()

    # Para manter o programa rodando enquanto o áudio toca
    while pygame.mixer.music.get_busy():
        pass


def Bip_Carregamento ():
    # Inicializa o mixer de som
    pygame.mixer.init()

    # Caminho para a pasta que contém os arquivos de áudio
    caminho_pasta = "/home/levs/Músicas/Bips/Bips de carregamento/"

    # Obtém uma lista de todos os arquivos na pasta
    arquivos_audio = [f for f in os.listdir(caminho_pasta) if f.endswith('.mp3')]

    # Escolhe um arquivo aleatório
    arquivo_escolhido = choice(arquivos_audio)

    # Caminho completo para o arquivo de áudio escolhido
    caminho_arquivo = os.path.join(caminho_pasta, arquivo_escolhido)

    # Carrega o arquivo de áudio
    pygame.mixer.music.load(caminho_arquivo)

    # Reproduz o áudio
    pygame.mixer.music.play()

    # Para manter o programa rodando enquanto o áudio toca
    while pygame.mixer.music.get_busy():
        pass


def Bip_Inicialização ():
    # Inicializa o mixer de som
    pygame.mixer.init()

    # Caminho para a pasta que contém os arquivos de áudio
    caminho_pasta = "/home/levs/Músicas/Bips/Bip de inicialização/"

    # Obtém uma lista de todos os arquivos na pasta
    arquivos_audio = [f for f in os.listdir(caminho_pasta) if f.endswith('.mp3')]

    # Escolhe um arquivo aleatório
    arquivo_escolhido = choice(arquivos_audio)

    # Caminho completo para o arquivo de áudio escolhido
    caminho_arquivo = os.path.join(caminho_pasta, arquivo_escolhido)

    # Carrega o arquivo de áudio
    pygame.mixer.music.load(caminho_arquivo)

    # Reproduz o áudio
    pygame.mixer.music.play()

    # Para manter o programa rodando enquanto o áudio toca
    while pygame.mixer.music.get_busy():
        pass


def Bip_Notificação ():
    # Inicializa o mixer de som
    pygame.mixer.init()

    # Caminho para a pasta que contém os arquivos de áudio
    caminho_pasta = "/home/levs/Músicas/Bips/Bip de notificação/"

    # Obtém uma lista de todos os arquivos na pasta
    arquivos_audio = [f for f in os.listdir(caminho_pasta) if f.endswith('.mp3')]

    # Escolhe um arquivo aleatório
    arquivo_escolhido = choice(arquivos_audio)

    # Caminho completo para o arquivo de áudio escolhido
    caminho_arquivo = os.path.join(caminho_pasta, arquivo_escolhido)

    # Carrega o arquivo de áudio
    pygame.mixer.music.load(caminho_arquivo)

    # Reproduz o áudio
    pygame.mixer.music.play()

    # Para manter o programa rodando enquanto o áudio toca
    while pygame.mixer.music.get_busy():
        pass
    
    
def Bip_erro ():
    # Inicializa o mixer de som
    pygame.mixer.init()

    # Caminho para a pasta que contém os arquivos de áudio
    caminho_pasta = "/home/levs/Músicas/Bips/Bip de Erro/"

    # Obtém uma lista de todos os arquivos na pasta
    arquivos_audio = [f for f in os.listdir(caminho_pasta) if f.endswith('.mp3')]

    # Escolhe um arquivo aleatório
    arquivo_escolhido = choice(arquivos_audio)

    # Caminho completo para o arquivo de áudio escolhido
    caminho_arquivo = os.path.join(caminho_pasta, arquivo_escolhido)

    # Carrega o arquivo de áudio
    pygame.mixer.music.load(caminho_arquivo)

    # Reproduz o áudio
    pygame.mixer.music.play()

    # Para manter o programa rodando enquanto o áudio toca
    while pygame.mixer.music.get_busy():
        pass


def Bip_logout ():
    # Inicializa o mixer de som
    pygame.mixer.init()

    # Caminho para a pasta que contém os arquivos de áudio
    caminho_pasta = "/home/levs/Músicas/Bips/Bip logout/"

    # Obtém uma lista de todos os arquivos na pasta
    arquivos_audio = [f for f in os.listdir(caminho_pasta) if f.endswith('.mp3')]

    # Escolhe um arquivo aleatório
    arquivo_escolhido = choice(arquivos_audio)

    # Caminho completo para o arquivo de áudio escolhido
    caminho_arquivo = os.path.join(caminho_pasta, arquivo_escolhido)

    # Carrega o arquivo de áudio
    pygame.mixer.music.load(caminho_arquivo)

    # Reproduz o áudio
    pygame.mixer.music.play()

    # Para manter o programa rodando enquanto o áudio toca
    while pygame.mixer.music.get_busy():
        pass
