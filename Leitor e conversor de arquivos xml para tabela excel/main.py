# pip install xmltodict numpy openpyxl pandas
import xmltodict
import os
import pandas as pd

def pegar_infos(nome_arquivo, valores):
    # Abre o arquivo XML correspondente dentro do diretório 'nfs', lê o conteúdo
    # e transforma o XML em um dicionário Python chamado 'dic_arquivo'.
    with open(f'nfs/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)

        # Verifica se a chave "NFe" está presente no dicionário 'dic_arquivo'.
        # Se sim, atribui as informações da nota fiscal a 'infos_nf'.
        # Caso contrário, assume que a chave é 'nfeProc' e acessa as informações.
        if "NFe" in dic_arquivo:
            infos_nf = dic_arquivo["NFe"]['infNFe']
        else:
            infos_nf = dic_arquivo['nfeProc']["NFe"]['infNFe']

        # Extrai o número da nota, o nome da empresa emissora, o nome do cliente,
        # o endereço de destino e o peso da carga (se disponível).
        numero_nota = infos_nf["@Id"]
        empresa_emissora = infos_nf['emit']['xNome']
        nome_cliente = infos_nf["dest"]["xNome"]
        endereco = infos_nf["dest"]["enderDest"]

        # Verifica se a chave "vol" está presente nas informações de transporte.
        # Se sim, extrai o peso da carga. Caso contrário, define como "Não informado".
        if "vol" in infos_nf["transp"]:
            peso = infos_nf["transp"]["vol"]["pesoB"]
        else:
            peso = "Não informado"

        # Adiciona as informações extraídas à lista 'valores'.
        valores.append([numero_nota, empresa_emissora, nome_cliente, endereco, peso])

# Obtém a lista de arquivos no diretório 'nfs'.
lista_arquivos = os.listdir("nfs")

# Define as colunas desejadas para o DataFrame.
colunas = ["numero_nota", "empresa_emissora", "nome_cliente", "endereco", "peso"]
valores = []

# Itera sobre cada arquivo na lista de arquivos e chama a função 'pegar_infos'
# para extrair as informações e adicioná-las à lista 'valores'.
for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)

# Cria um DataFrame usando as colunas e valores coletados e o converte em um arquivo Excel.
tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel("NotasFiscais.xlsx", index=False)
