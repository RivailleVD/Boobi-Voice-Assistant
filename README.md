## Reconhecimento de Voz com Vosk 🎙️
Este projeto explora as capacidades do Vosk, uma ferramenta de reconhecimento de voz offline open-source, e demonstra como integrá-la em aplicações Python de forma personalizada e eficiente.

### 📚 Sobre o Projeto
O objetivo deste projeto é proporcionar um exemplo prático de integração do Vosk com Python, permitindo o reconhecimento de voz de maneira eficaz e sem a necessidade de conexão com a internet.

### ⚙️ Funcionalidades
* **Reconhecimento de voz offline:** Processamento de áudio completamente local, sem necessidade de internet.
* **Suporte a múltiplos idiomas:** Fácil adaptação para diferentes línguas e dialetos.
* **Integração simplificada com Python:** Uso de bibliotecas Python para rápida implementação e execução.

### 🚀 Como Instalar

*Clone o repositório:*
 **git clone https://github.com/RivailleVD/Boobi-Voice-Assistant.git**
**cd Boobi-Voice-Assistant**

### Ative o ambiente virtual:

**source ambientevirt2/bin/activate**

### Caso queira criar um novo ambiente virtual, instale as dependências necessárias com:

**pip install -r requirements.txt**

## 🔧 Configurações Importantes

* **Caminho para o Modelo Vosk:**

Ao configurar o ambiente, ajuste o caminho para o modelo do Vosk em Recognition/reconhecimento03.py na linha 14:

    model = vosk.Model(r'Seu caminho para o modelo de reconhecimento')  # Defina o caminho para o modelo Vosk

* **Caminho para os Arquivos de Áudio:**

No arquivo Bips/Bips.py, você deve definir o caminho correto para os arquivos de áudio salvos em pastas específicas. Por exemplo:

    python
    Copiar código
    def Bip_aleatorio():
        # Inicializa o mixer de som
        pygame.mixer.init()
    
        # Caminho para a pasta de áudios
        caminho_pasta = "CAMINHO PARA A PASTA COM BIPS CORRESPONDENTES"
    
        # Lista os arquivos de áudio da pasta
        arquivos_audio = [f for f in os.listdir(caminho_pasta) if f.endswith('.mp3')]
    
        # Escolhe um arquivo aleatório
        arquivo_escolhido = choice(arquivos_audio)
    
        # Caminho completo para o arquivo de áudio
        caminho_arquivo = os.path.join(caminho_pasta, arquivo_escolhido)
    
        # Carrega e reproduz o áudio
        pygame.mixer.music.load(caminho_arquivo)
        pygame.mixer.music.play()
    
        # Mantém o programa ativo enquanto o áudio toca
        while pygame.mixer.music.get_busy():
            pass

  em "caminho_pasta" defina o caminho correto para os arquivos de audio salvos na pasta "Bips" de acordo com cada função correspondente ao nome da pasta.

  ## ▶️ Executando a Aplicação
Depois de concluir todas as configurações, execute o arquivo main.py para iniciar a aplicação:

    python
    main.py

## 📝 Observações
Este projeto foi desenvolvido e personalizado para funcionar no Linux Kubuntu. Caso deseje utilizar em outro sistema operacional, pode ser necessário fazer pequenas adaptações no código. Sinta-se à vontade para modificar o código conforme seus requisitos e personalizar as funcionalidades de automação.
