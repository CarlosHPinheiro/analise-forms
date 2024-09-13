# Análise de Formulários

O programa foi desenvolvido com o intuito de gerar um relatório através de dados extraídos de uma pesquisa de satisfação de clientes implementada através de formulários. Os dados da pesquisa foram exportados em um arquivo `.csv`.

O programa faz a leitura do arquivo `.csv` e cria um relatório dos dados extraídos retornando uma pasta com os dados da pesquisa estruturados em uma planilha no formato `.xlsx` padrão excel.

Para cada categoria de perguntas do formulário é gerado um gráfico com a análise percentual de acordo com as respostas coletadas através dos formulários.

-   [Modelo de formulário utilizado](https://dfsdf.com.br)

-   [Exemplo do formato extraído dos formulários](dfsdfsdfs)

## Tecnologias Utilizadas

-   **Python** - https://www.python.org/
    -   `Pandas` - https://pandas.pydata.org/docs/index.html
    -   `MatplotLib` - https://matplotlib.org/
    -   `Shutil` - https://docs.python.org/3/library/shutil.html
    -   `Os` - https://docs.python.org/pt-br/3/library/os.html

### Dependências e Versões

-   `contourpy==1.3.0`
-   `cycler==0.12.1`
-   `et-xmlfile==1.1.0`
-   `fonttools==4.53.1`
-   `kiwisolver==1.4.7`
-   `matplotlib==3.9.2`
-   `numpy==2.1.1`
-   `openpyxl==3.1.5`
-   `packaging==24.1`
-   `pandas==2.2.2`
-   `pillow==10.4.0`
-   `pyparsing==3.1.4`
-   `python-dateutil==2.9.0.post0`
-   `pytz==2024.2`
-   `six==1.16.0`
-   `tzdata==2024.1`

### Como rodar o projeto

Para rodar o projeto, siga as instruções abaixo para configurar o ambiente e instalar as dependências necessárias.

**Clone o Repositório**

Primeiro, clone o repositório para sua máquina local usando o Git. Abra um terminal e execute o comando:

```
git clone https://github.com/CarlosHPinheiro/analise-forms.git
cd repositorio
```

**Crie um Ambiente Virtual (Recomendado)**

Esse não é um passo obrigatório mas é recomendado a criação de um ambiente virtual para gerenciar as dependências do projeto.

Para criar um ambiente virtual, execute:

```
python -m venv venv
```

**Ative o ambiente virtual**

-   Sistema Operacional Windows:

```
venv\Scripts\activate
```

-   Sistema Operacional MacOs e Linux:

```
source venv/bin/activate
```

**Instale as dependências**

Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt` utilizando com o seguinte comando:

```
pip install -r requirements.txt
```

**Arquivo** `.csv`

O modelo de arquivo `.csv` utilizado pode ser encontrado dentro da pasta `csv` nomeado como `formulario-modelo.csv`. Para utilizá-lo basta renomeá-lo como `formulario.csv`.

**Execute o programa**

Após concluir os passos anteriores, para rodar o programa execute o comando:

```
python app.py
```

**Após a execução**

Após a execução do programa é criada uma pasta `Relatório` contendo um arquivo excel `planilha.xlsx` com os dados extraídos da análise organizados em uma planilha e os arquivos `png` com os gráficos referentes a cada categoria contendo o percentual de cada resposta colhida através dos formulários.
