import whisper
import os
from tkinter import Tk, Button, Label, Toplevel, filedialog, messagebox
from time import time
import sys

# 2025 AudioTranscrissor por pasta
# Versão: 1.7. Elaboração: Investigador Fabio Nunes Coelho. Todos os direitos reservados.


def escolher_modelo_interface():
    """ Exibe uma interface para escolher o modelo Whisper e retorna o modelo selecionado. """
    root = Tk()
    root.withdraw()
    modelo_escolhido = None

    def selecionar_modelo(modelo):
        nonlocal modelo_escolhido
        modelo_escolhido = modelo
        janela.destroy()
        root.quit()

    janela = Toplevel(root)
    janela.title("Escolha o Modelo Whisper")

    Label(janela, text="Escolha o modelo Whisper:", font=("Arial", 14)).pack(pady=10)

    for modelo in ["tiny", "base", "small", "medium", "large"]:
        Button(janela, text=modelo.capitalize(), font=("Arial", 12),
               command=lambda m=modelo: selecionar_modelo(m)).pack(pady=5)

    janela.protocol("WM_DELETE_WINDOW", lambda: (janela.destroy(), root.quit()))
    janela.mainloop()

    return modelo_escolhido

def selecionar_pasta():
    """ Abre um diálogo para selecionar uma pasta e retorna seu caminho. """
    Tk().withdraw()
    return filedialog.askdirectory(title="Selecione a pasta com os arquivos de áudio")

def exibir_mensagem(titulo, mensagem):
    """ Exibe uma caixa de mensagem ao usuário. """
    messagebox.showinfo(titulo, mensagem)

def listar_arquivos_audio(pasta):
    """ Lista todos os arquivos de áudio na pasta selecionada e imprime para depuração. """
    print(f"\n📂 Verificando arquivos na pasta: {pasta}")

    # Listar TODOS os arquivos na pasta
    todos_os_arquivos = os.listdir(pasta)
    print(f"📝 Arquivos encontrados na pasta:\n{todos_os_arquivos}\n")

    # Formatos aceitos, incluindo `.opus`
    formatos_audio = (".ogg", ".mp3", ".wav", ".m4a", ".aac", ".flac", ".opus")
    arquivos = [f for f in todos_os_arquivos if f.lower().endswith(formatos_audio)]

    if not arquivos:
        print(f"🚨 Nenhum arquivo de áudio válido encontrado na pasta {pasta}.")
    else:
        print(f"🎵 Arquivos de áudio detectados ({len(arquivos)}):")
        for arquivo in arquivos:
            print(f"  - {arquivo}")

    return arquivos

def transcrever_audio(modelo, arquivo_audio):
    """ Transcreve o áudio usando o modelo selecionado e retorna o texto transcrito. """
    print(f"Iniciando transcrição: {arquivo_audio}")

    try:
        resultado = modelo.transcribe(arquivo_audio, language="pt")
        return resultado
    except Exception as e:
        print(f"❌ Erro ao transcrever {arquivo_audio}: {e}")
        return None

def salvar_transcricao(arquivo_audio, resultado, pasta_saida):
    """ Salva a transcrição em um arquivo de texto dentro da pasta de saída. """
    nome_arquivo = os.path.basename(arquivo_audio).rsplit(".", 1)[0] + "_transcricao.txt"
    caminho_saida = os.path.join(pasta_saida, nome_arquivo)

    try:
        with open(caminho_saida, "w", encoding="utf-8") as arquivo:
            arquivo.write("=== TRANSCRIÇÃO DO ÁUDIO ===\n\n")
            arquivo.write(resultado["text"] + "\n")
            arquivo.write("\n=== FIM DA TRANSCRIÇÃO ===\n")
            arquivo.write("\n============================\n")
            arquivo.write("\n=== 2025 AudioTranscrissor Versão: 1.7.===\n")
            arquivo.write("\n=== Elaboração: Investigador Fabio Nunes Coelho.===\n")
            arquivo.write("\n=== ®Todos os direitos reservados. ===\n")

        print(f"✅ Transcrição salva em: {caminho_saida}")
    except Exception as e:
        print(f"❌ Erro ao salvar a transcrição de {arquivo_audio}: {e}")

# Fluxo principal
if __name__ == "__main__":
    try:
        # Escolher modelo Whisper
        modelo_escolhido = escolher_modelo_interface()
        if not modelo_escolhido:
            exibir_mensagem("Erro", "Nenhum modelo selecionado. Encerrando o programa.")
            sys.exit(1)

        print(f"Modelo selecionado: {modelo_escolhido}")
        print(f"Carregando o modelo Whisper '{modelo_escolhido}'...")

        try:
            modelo = whisper.load_model(modelo_escolhido)
        except Exception as e:
            exibir_mensagem("Erro", f"Erro ao carregar o modelo '{modelo_escolhido}': {e}")
            sys.exit(1)

        print("✅ Modelo carregado com sucesso!")

        # Selecionar a pasta contendo os arquivos de áudio
        pasta_audio = selecionar_pasta()
        if not pasta_audio:
            exibir_mensagem("Erro", "Nenhuma pasta selecionada. Encerrando o programa.")
            sys.exit(1)

        print(f"📂 Pasta selecionada: {pasta_audio}")

        # Listar arquivos de áudio
        arquivos_audio = listar_arquivos_audio(pasta_audio)
        if not arquivos_audio:
            exibir_mensagem("Erro", "Nenhum arquivo de áudio encontrado na pasta selecionada.")
            sys.exit(1)

        # Criar uma pasta para salvar as transcrições
        pasta_saida = os.path.join(pasta_audio, "transcricoes")
        os.makedirs(pasta_saida, exist_ok=True)

        # Processar todos os arquivos de áudio na pasta
        for arquivo in arquivos_audio:
            caminho_arquivo = os.path.join(pasta_audio, arquivo)
            inicio = time()
            resultado = transcrever_audio(modelo, caminho_arquivo)
            if resultado:
                tempo_execucao = time() - inicio
                print(f"✅ Transcrição de {arquivo} concluída em {tempo_execucao:.2f} segundos.")
                salvar_transcricao(caminho_arquivo, resultado, pasta_saida)

        exibir_mensagem("Sucesso", f"Transcrições concluídas! Arquivos salvos em '{pasta_saida}'.")

    finally:
        print("🛑 Finalizando programa...")
