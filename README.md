# 🎤 AudioTranscrissor v1.7 – Transcritor de Áudios do WhatsApp

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()
[![OpenAI Whisper](https://img.shields.io/badge/ASR-Whisper-black.svg)]()

## 📌 Contexto e Motivação
Durante operações policiais, realizo **extrações de celulares apreendidos** (com ordem judicial).  
No **WhatsApp**, é comum encontrar **centenas de áudios**, que precisam ser ouvidos para levantar provas contra os suspeitos.  
Esse processo manual pode levar **semanas**.

Os transcrissores disponíveis na internet, além de pagos ou limitados nas versões gratuitas, permitem **transcrever apenas um áudio por vez**, o que inviabiliza o trabalho em larga escala.

➡️ A solução foi desenvolver um **transcritor gratuito**, em **Python**, que transcreve **vários áudios de uma só vez**, otimizando o processo de investigação.

---

## 🎯 Objetivos
- Ferramenta **gratuita e simples** para transcrever áudios, especialmente de **conversas do WhatsApp**.  
- **Processamento em lote** (vários áudios em uma pasta).  
- Redução do tempo de elaboração de relatórios policiais e investigativos.  

---

## 🚀 Resultados
- Transcrição de **pastas inteiras** de uma só vez.  
- Redução de tempo em **até 2/3** vs. processo manual.  
- Mantém a necessidade de **validação/revisão**, ainda assim **acelera consideravelmente**.

---

## ⚙️ Funcionalidades
- Interface gráfica (Tkinter) para escolher **modelo Whisper** e **pasta com áudios**.  
- Suporte a `.ogg`, `.mp3`, `.wav`, `.m4a`, `.aac`, `.flac`, `.opus`.  
- Criação automática da pasta `transcricoes/` com `.txt`.  
- Cabeçalho/rodapé com **versão** e **autoria**.  

---

## 🛠️ Tecnologias
- Python 3.9+
- OpenAI Whisper
- PyTorch
- Tkinter (nativo)
- **ffmpeg** (no sistema)

---

## 📦 Instalação

> Windows (VS Code recomendado)

1. Instalar o Vs Code, disponível na pasta ou baixar em:
https://code.visualstudio.com/docs/?dv=win64user

2. Instalar extensões para PTBR dentro do VS Code em "Extensões";

3. Instalar o Python vs Python 3.12.8 disponível na pasta ou baixar em:
https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe
  OBS. Marcar PATH na instalação;

4. Instalar openai-whisper pelo terminal do Vs Code (Ctrl + '):
    Digite o comando no terminal: pip install openai-whisper

Obs.: caso não funcione, reinstalar biblioteca "openai-whisper"

5. instalar ffmpeg disponível na pasta ou baixar em: ffmpeg:https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z
    descompactar e renomear para "ffmpeg" em seguida colar no disco C:\

    executar o cmd como ADM e executar o código: setx /m PATH "C:\ffmpeg\bin;%PATH%"
        deve aparecer a frase "êxito: o valor especificado foi salvo"

6. feche e abra o VS Code. caso não funcione, reiniciar o sistema operacional
    Para verificar se o FFmpeg já está sendo reconhecido, digitar no terminal: ffmpeg 
     a mensagem não pode aparecer como:
        "ffmpeg não é um comando reconhecido", diferente disso, estará instalado correto;

7. Execute o arquivo AudioTranscrissor_v1.7.py pelo  VS Code;

8. No canto superior (lado onde fecha a tela) clicar no Triangulo "Executar arquivo do Python" e aguarde.

9. Escolha o modelo e aguarde baixar. Obs. Será necessária baixar apenas uma vez. O download do modelo será necessário apenas uma vez. As transcrições posteriores, os modelos já estarão baixado e prontos para uso.

				>>talela modelo<<
  		 SIZE       Parametro   Uso VRAM    Velocidade   
  		 tiny:      39 M;       1GB;         32x
  		 base:      74 M;       1GB;         16x
       small:     244 M;      2GB;         6x
   	 medium:    769 M;      5GB;         2x
   	 large:     1550 M;     10GB;        1x

Recomendo baixar os modelos small e medium, pois oferecem uma boa transcrição. No entanto, se quiser baixar todos e ir testando, fique à vontade.
Quanto menor o modelo, menores serão os requisitos do computador e mais rápido será o processo. Porém, neste caso, a qualidade da transcrição será baixa.
Se optar pelo modelo mais elevado, as transcrições serão mais assertivas.
 
10. Após escolher o modelo e concluído o download, selecione a pasta com os arquivos no formato original do WhatsApp (.opus), clique em Abrir e aguarde a transcrição ser finalizada.

Observação: É normal não visualizar nenhum arquivo. Ignore essa ausência e clique em Selecionar pasta. 

11. Após a transcrição, uma tela indicará "Sucesso", informando o local da pasta transcrições (no mesmo diretório de origem dos áudios).

12. Clique em OK para finalizar o programa e confira se os dados das transcrições nos arquivos .txt correspondem aos áudios transcritos. Cada arquivo .txt terá o mesmo nome do seu respectivo áudio.
   

## 📸 Evidências Visuais

### Página inicial do repositório
![Home do repositório](docs/img/repo_home.png)

### Histórico de commits
![Commits](docs/img/commits.png)

### Release publicada
![Release](docs/img/release.png)

### Execução da ferramenta
![Execução](docs/img/execution_gui.png)
