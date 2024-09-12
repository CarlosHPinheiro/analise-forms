import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV e cria o DataFrame
form_df = pd.read_csv('csv/formulario.csv')

# Renomeia as colunas
form_df = form_df.rename(columns={
    'Carimbo de data/hora': 'Data/Hora',
    'Você costuma comprar regularmente neste estabelecimento?': 'Cliente Frequente',
    'Como você avalia a variedade de produtos disponíveis?': 'Variedade dos Produtos',
    'Como você avalia a qualidade dos produtos oferecidos?': 'Qualidade',
    'Como você avalia os preços dos nossos produtos?': 'Preços',
    'Como você avalia a limpeza do nosso estabelecimento?': 'Limpeza',
    'Como você avalia o atendimento dos nossos funcionários?': 'Atendimento'
})

# Cria a variável que contém o período em que os dados foram coletados
periodo = f"Dados coletados de {form_df['Data/Hora'].iloc[0]}  a  {form_df['Data/Hora'].iloc[-1]}\n"

# Cria a pasta 'graficos' se ela não existir
pasta_graficos = 'graficos'
if not os.path.exists(pasta_graficos):
    os.makedirs(pasta_graficos)

# Itera sobre as colunas e cria um gráfico de pizza para cada uma
for coluna in form_df.columns[1:]:  # Pula a coluna "Data/Hora"
    plt.figure(figsize=(12, 12))
    contagem = form_df[coluna].value_counts()
    contagem.plot.pie(autopct='%1.1f%%')
    plt.title(f'{periodo}\n{coluna}')
    plt.ylabel('')  # Remove o rótulo do eixo Y

    # Define o caminho completo do arquivo
    arquivo_grafico = os.path.join(pasta_graficos, f'{coluna}.png')

    plt.savefig(arquivo_grafico)
    plt.close()

# Cria um arquivo xlsx com o DataFrame
form_df.to_excel('planilha.xlsx', index=False, sheet_name='Data Frame')

# Organizar os arquivos gerados
# Definir os nomes dos diretórios e arquivos
pasta_graficos = 'graficos'
arquivo_planilha = 'planilha.xlsx'
diretorio_relatorio = 'Relatório'

if not os.path.exists(diretorio_relatorio):
    os.makedirs(diretorio_relatorio)

# Mover a pasta 'graficos' para o diretório 'Relatório'
novo_caminho_graficos = os.path.join(diretorio_relatorio, pasta_graficos)
if os.path.exists(pasta_graficos):
    shutil.move(pasta_graficos, novo_caminho_graficos)
else:
    print(f"A pasta {pasta_graficos} não existe.")

# Mover o arquivo 'planilha.xlsx' para o diretório 'Relatório'
novo_caminho_planilha = os.path.join(diretorio_relatorio, arquivo_planilha)
if os.path.exists(arquivo_planilha):
    shutil.move(arquivo_planilha, novo_caminho_planilha)
else:
    print(f"O arquivo {arquivo_planilha} não existe.")

print("Os arquivos foram gerados e organizados na pasta Relatório")
