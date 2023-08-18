import PyPDF2  # Importa o módulo PyPDF2, que permite trabalhar com arquivos PDF.
import os  # Importa o módulo os, que fornece funções relacionadas ao sistema operacional, como listagem de arquivos em diretórios.

merger = PyPDF2.PdfMerger()  # Cria um objeto PdfMerger que será usado para mesclar os arquivos PDF.

lista_arquivos = os.listdir("arquivos")  # Lista os arquivos presentes no diretório "arquivos" e armazena-os em uma lista.
lista_arquivos.sort()  # Ordena a lista de arquivos em ordem alfabética.

print(lista_arquivos)  # Imprime a lista de arquivos presentes no diretório "arquivos" (apenas para fins de visualização).

for arquivo in lista_arquivos:  # Inicia um loop para cada arquivo na lista de arquivos.
    if ".pdf" in arquivo:  # Verifica se o arquivo possui a extensão ".pdf".
        merger.append(f"arquivos/{arquivo}")  # Adiciona o arquivo PDF atual à operação de mesclagem.

merger.write("PDF Final.pdf")  # Realiza a operação de mesclagem dos arquivos PDF e cria um novo arquivo chamado "PDF Final.pdf".
