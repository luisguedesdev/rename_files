import os

def renomear_videos(diretorio_principal):
    extensoes_video = ('.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.mpeg')
    
    for raiz, subdirs, arquivos in os.walk(diretorio_principal):
        nome_pasta = os.path.basename(raiz)
        videos = [arquivo for arquivo in arquivos if arquivo.lower().endswith(extensoes_video)]
        
        for idx, video in enumerate(videos, start=1):
            extensao = os.path.splitext(video)[1]
            novo_nome = f"{nome_pasta}{f'_{idx}' if len(videos) > 1 else ''}{extensao}"
            caminho_antigo = os.path.join(raiz, video)
            caminho_novo = os.path.join(raiz, novo_nome)
            
            try:
                os.rename(caminho_antigo, caminho_novo)
                print(f"Renomeado: {caminho_antigo} -> {caminho_novo}")
            except Exception as e:
                print(f"Erro ao renomear {caminho_antigo}: {e}")

# Defina o caminho da pasta principal onde estão os vídeos
diretorio = ""
renomear_videos(diretorio)
