import os  # Importa o módulo os, que fornece funções relacionadas ao sistema operacional.
from tkinter.filedialog import askdirectory  # Importa a função askdirectory do módulo tkinter.filedialog, que permite exibir uma caixa de diálogo para selecionar um diretório.

# Pede ao usuário para selecionar uma pasta através de uma caixa de diálogo e armazena o caminho da pasta selecionada em 'caminho'.
caminho = askdirectory(title="Selecione uma pasta")

# Lista os arquivos presentes no diretório selecionado e armazena-os em uma lista chamada 'lista_arquivos'.
lista_arquivos = os.listdir(caminho)

# Dicionário 'locais' que contém chaves correspondentes a tipos de arquivos e valores são listas de suas respectivas extensões.
locais = {
    "pdf": [".pdf"],
    "imagens": [".jpg", ".png", ".gif"],
    "documentos": [".docx", ".xlsx", ".pptx"],
    "audio": [".mp3", ".wav", ".flac"],
    "video": [".mp4", ".avi", ".mov"],
    "compactados": [".zip", ".rar", ".7z"],
    "texto": [".txt", ".csv", ".md"],
    "codigos": [".py", ".java", ".cpp"],
    "planilhas": [".xls", ".ods", ".csv"],
    "apresentacoes": [".ppt", ".key", ".odp"],
    "ebooks": [".epub", ".mobi", ".azw"],
    "fontes": [".ttf", ".otf", ".woff"],
    "executaveis": [".exe", ".dmg", ".app"],
    "imagens_vetoriais": [".svg", ".ai", ".eps"],
    "bases_de_dados": [".sql", ".sqlite", ".db"],
    "html": [".html", ".htm"],
    "css": [".css"],
    "javascript": [".js"],
    "xml": [".xml"],
    "json": [".json"],
    "php": [".php"],
    # Adicione mais tipos de arquivo aqui
}

# Inicia um loop para cada arquivo na lista de arquivos.
# Loop que itera através de cada arquivo na lista de arquivos do diretório
for arquivo in lista_arquivos:
    # Divide o nome do arquivo e a extensão usando a função splitext do módulo os.path
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")

    # Itera através dos tipos de arquivo definidos no dicionário locais
    for pasta in locais:
        # Verifica se a extensão do arquivo está presente nas extensões do tipo de arquivo
        if extensao in locais[pasta]:
            # Obtém a extensão sem o ponto inicial
            pastaExtensao = extensao[1:]
            
            # Monta o caminho completo para a pasta final onde o arquivo será movido
            caminho_pasta_final = f"{caminho}/{pasta}/{pastaExtensao.upper()}"
            
            # Cria a estrutura de pastas necessárias, se ainda não existirem
            os.makedirs(caminho_pasta_final, exist_ok=True)
            
            # Monta os caminhos completos para o arquivo original e o arquivo final
            caminho_arquivo_original = f"{caminho}/{arquivo}"
            caminho_arquivo_final = f"{caminho_pasta_final}/{arquivo}"
            
            # Verifica se o arquivo original ainda existe no diretório
            if os.path.exists(caminho_arquivo_original):
                # Move o arquivo para o local final
                os.rename(caminho_arquivo_original, caminho_arquivo_final)

