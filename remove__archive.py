import os

# Defina o caminho da pasta onde os arquivos estão localizados
pasta = "D:/Onedrive/HQs/A Saga do Batman"  # Substitua pelo caminho correto

# Percorre todos os arquivos na pasta
for arquivo in os.listdir(pasta):
    caminho_antigo = os.path.join(pasta, arquivo)
    
    # Verifica se é um arquivo (e não uma pasta)
    if os.path.isfile(caminho_antigo):
        # Substitui '_' por espaço no nome do arquivo
        novo_nome = arquivo.replace('_', ' ')
        caminho_novo = os.path.join(pasta, novo_nome)

        # Verifica se o novo nome já existe para evitar conflitos
        if not os.path.exists(caminho_novo):
            os.rename(caminho_antigo, caminho_novo)
            print(f'Renomeado: "{arquivo}" → "{novo_nome}"')
        else:
            print(f'Erro: "{novo_nome}" já existe. Verifique antes de renomear.')
