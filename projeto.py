import pandas as pd

df = pd.read_csv("cat_acidentes.csv", sep=";")
df.head()
df_tratado = df.copy()

df.shape

# A base possui 75.176 registros e 34 colunas, indicando um volume significativo de informações para análise.

df.info()

# Observa-se a presença cionadas a datas, poderão necessitar de conversão de tipo para facilitar análises temporais.de colunas numéricas, categóricas e geográficas. Algumas colunas, especialmente as relacionadas a datas, poderão necessitar de conversão de tipo para facilitar análise temporais.

df.isnull().sum()

# Foi identificada a existência de dados ausentes em algumas variáveis. Essas colunas serão avaliadas posteriormente para decidir se os valores serão removidos ou preenchidos.

df.columns

# As principais variáveis da base incluem data do acidente, região, tipo de acidente, quantidade de vítimas, veículos envolvidos e localização geográfica.

df['tipo_acid'].value_counts().head()

# A exploração inicial mostra que alguns tipos de acidentes aparecem com maior frequência do que outros. Essa informação será utilizada posteriormente para identificar quais ocorrências são mais comuns na base.

df['regiao'].value_counts()

# Observa-se que os registros não estão distribuídos igualmente entre as regiões, indicando possíveis diferenças na concentração de acidentes.

df['dia_sem'].value_counts()

# A distribuição dos acidentes ao longo dos dias da semana sugere variações que poderão ser analisadas mais detalhadamente nas próximas etapas.

df.describe()

# As estatísticas descritivas mostram informações como média, desvio padrão, valores mínimos e máximos das variáveis numéricas. Observa-se que algumas variáveis representam contagens de vítimas, veículos envolvidos e coordenadas geográficas dos acidentes.

## Dificuldades Encontradas

# Durante o carregamento da base foi necessário identificar o separador correto do arquivo CSV, utilizando o parâmetro `sep=";"`. Também foram identificados valores ausentes em algumas colunas, o que exigirá análise e tratamento nas próximas etapas do trabalho. Além disso, algumas variáveis possuem nomes abreviados, sendo necessário compreender seu significado antes da realização das análises.


# **PARTE 2**

df_tratado['noite_dia'] = pd.get_dummies(df['noite_dia'], drop_first=True)

print(df_tratado)

df.info()


print(df)

print(df['log1'])

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df_tratado["log1"] = le.fit_transform(df_tratado["log1"].astype(str))

print(df_tratado)


print(df_tratado['log1'])
# USE print(le.inverse_transform([CÓDIGO DA RUA])) PARA SABER QUAL RUA ESTÁ RELACIONADA AO CÓDIGO.