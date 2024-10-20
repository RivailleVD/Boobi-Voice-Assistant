import pyaudio
import vosk
import json
import logging
from Funções.Automação import *
from Funções.front import *
from Funções.manual import *
from Bips.Bips import Bip_logout , Bip_aleatorio
from time import sleep

def reconhecimento_continuo():
    # Inicializa o Vosk com o modelo 
    logging.getLogger("VoskAPI").setLevel(logging.ERROR)
    model = vosk.Model(r'Seu caminho para o modelo de reconhecimento')  # Ajuste o caminho do modelo
    recognizer = vosk.KaldiRecognizer(model, 44100)

    # Configurações do PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)

    # Inicia o stream de áudio
    
    stream.start_stream()
    front()
    sleep(2)
    manual()
    print("Iniciando o reconhecimento de voz... Fale algo!")

    try:
        while True:
            data = stream.read(1024)  # Ler o áudio
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                result_dict = json.loads(result)
                if result_dict.get('confidence', 1.0) > 0.7 and 'text' in result_dict:  # Adicione um limite de confiança
                    recognized_text = result_dict['text']
                    print("Você disse:", recognized_text)
                    
                
                if 'text' in result_dict and result_dict['text']:  # Verifica se há texto reconhecido
                    recognized_text = result_dict['text']  # Armazena o texto reconhecido
                    print("Você disse:", recognized_text)  # Exibe o texto reconhecido
                    
                    # Aqui você pode realizar qualquer ação com o texto reconhecido
                    
                    #if 'paz do senhor' in recognized_text.lower():
                        #print("Deus abençoe")
                        

                    #verifica a ativação da Função "abrir Calculadora"
                    if 'abrir calculadora' in recognized_text.lower():
                        try:
                            # Tente abrir a calculadora, mas capture qualquer erro
                            abrircalculadora()
                        except AttributeError:
                            print("Função 'abrir_calculadora' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar abrir a calculadora: {e}")
                            
                    #verifica a ativação da Função "ligar teclado"
                    if 'ligar teclado' in recognized_text.lower():
                        try:
                            # Tente ligar o teclado mas capture qualquer erro
                            ligarteclado()
                        except AttributeError:
                            print("Função 'ligar teclado' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar ligar o teclado: {e}")
                            
                     #verifica a ativação da Função "apagar teclado"
                    if 'apagar teclado' in recognized_text.lower():
                        try:
                            # Tente ligar o teclado mas capture qualquer erro
                            apagarteclado()
                        except AttributeError:
                            print("Função 'apagar teclado' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar apagar o teclado: {e}")
                            
                       #verifica a ativação da Função "abrir code"
                    if 'abrir code' in recognized_text.lower():
                        try:
                            # Tente ligar o teclado mas capture qualquer erro
                            abrircode()
                        except AttributeError:
                            print("Função 'abrir code' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar abrir Code: {e}")
                            
                    '''#verifica a ativação da Função "abrir navegador"
                    if 'abrir navegador' in recognized_text.lower():
                        try:
                            # Tente abrir o navegador mas capture qualquer erro
                            abrirnavegador()
                        except AttributeError:
                            print("Função 'abrir navegador' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar abrir o Navegador: {e}")'''
                            
                    #verifica a ativação da Função "abrir mensageiro"
                    if 'abrir mensageiro' in recognized_text.lower():
                        try:
                            # Tente abrir o mensageiro mas capture qualquer erro
                            abrirmensageiro()
                        except AttributeError:
                            print("Função 'abrir mensageiro' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar abrir o mensageiro: {e}")
                        finally:
                            os.system('clear')
                            
                    '''#verifica a ativação da Função "abrir discord"
                    if 'abrir discorde' in recognized_text.lower():
                        try:
                            # Tente abrir o discord mas capture qualquer erro
                            abrirdiscord()
                        except AttributeError:
                            print("Função 'abrir discord' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar abrir o discord: {e}")'''
                            
                    '''#verifica a ativação da Função "abrir ficheiro"
                    if 'abrir o ficheiro' in recognized_text.lower():
                        try:
                            # Tente abrir o ficheiro mas capture qualquer erro
                            abrirficheiro()
                        except AttributeError:
                            print("Função 'abrir ficheiro' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar abrir o ficheiro: {e}")'''
                            
                    '''#verifica a ativação da Função "abrir krita"
                    if 'abrir crita' in recognized_text.lower():
                        try:
                            # Tente abrir o crita mas capture qualquer erro
                            abrirkrita()
                        except AttributeError:
                            print("Função 'abrir discord' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar abrir o discord: {e}")'''
                            
                            
                    #verifica a ativação da Função "alternar janela"
                    if 'alternar janela' in recognized_text.lower():
                        try:
                            # Tente alternar a janela mas capture qualquer erro
                            alternarjanela()
                        except AttributeError:
                            print("Função 'alternar janela' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar alternar a janela: {e}")
                            
                            
                     #funções de controle de multmidia para o YouTube      
                     #verifica a ativação da Função "avançar"
                    if 'avançar' in recognized_text.lower():
                        try:
                            # Tente avançar o video mas capture qualquer erro
                            avançar()
                        except AttributeError:
                            print("Função 'avançar' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar avançar o video: {e}")
                            
                    #verifica a ativação da Função "retroceder"
                    if 'retroceder' in recognized_text.lower():
                        try:
                            # Tente retroceder o video mas capture qualquer erro
                            retroceder()
                        except AttributeError:
                            print("Função 'retroceder' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar retroceder o video: {e}")
                            
                      #verifica a ativação da Função "pausar"
                    if 'pausar vídeo' in recognized_text.lower():
                        try:
                            # Tente pausar o video mas capture qualquer erro
                            pausa()
                        except AttributeError:
                            print("Função 'pausa' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar pausar o video: {e}")

                      #verifica a ativação da Função "reproduzir"       
                    if 'reproduzir video' in recognized_text.lower():
                        try:
                            # Tente reproduzir o video mas capture qualquer erro
                            reproduzir()
                        except AttributeError:
                            print("Função 'reproduzir' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar reproduzir o video: {e}")
                            
                    #funções para controle de multimidia com atalhos no teclado
                    #pode ser usado para controlar o reprodutor do smartphone com o KDE Conect    
                    #verifica a ativação da Função "pular"       
                    if 'próxima música' in recognized_text.lower():
                        try:
                            # Tente pular a musica mas capture qualquer erro
                            proximamusica()
                        except AttributeError:
                            print("Função 'pular' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar pular a música: {e}")
                            
                    if 'música anterior' in recognized_text.lower():
                        try:
                            # Tente voltar para a musica anterior mas capture qualquer erro
                            musicaanterior()
                        except AttributeError:
                            print("Função 'anterior' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar voltar a música: {e}")
                            
                    if 'para a música' in recognized_text.lower():
                        try:
                            # Tente parar a musica mas capture qualquer erro
                            pararmusica()
                        except AttributeError:
                            print("Função 'parar música' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar parar a música: {e}")
                            
                    if 'reproduzir música' in recognized_text.lower():
                        try:
                            # Tente parar a musica mas capture qualquer erro
                            reproduzirmusica()
                        except AttributeError:
                            print("Função 'reproduzir música' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar reproduzir a música: {e}")
                            
                    if 'manual' in recognized_text.lower():
                        try:
                            # Tente exibir o manual mas capture qualquer erro
                            manual()
                        except AttributeError:
                            print("Função 'manual' não encontrada. Continuando...")
                        except Exception as e:
                            print(f"Erro ao tentar exibir o manual: {e}")
                            
                            
                            
                                   
                                   
                            
                          
                    
                            
                        
                    if 'sair' in recognized_text.lower():
                        print("Comando de saída detectado. Encerrando...")
                        Bip_logout()
                        fechar(recognized_text)

                        break

            else:
                # Se o Vosk não reconhecer, você pode usar a saída parcial se desejar
                partial_result = recognizer.PartialResult()
                partial_dict = json.loads(partial_result)
                if 'partial' in partial_dict:
                    print("Reconhecendo:", partial_dict['partial'], end='\r')  # Atualiza a saída

    except KeyboardInterrupt:
        print("\nReconhecimento de voz interrompido.")

    


# Exemplo de uso:
#reconhecimento_continuo()


#def saida(recognized_text):
   #return   # Chama ouvir e retorna o texto capturado