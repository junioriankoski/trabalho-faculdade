# PARTE 2 — TRATAMENTO E PREPARAÇÃO DOS DADOS
from dados import df, df_tratado, pd

df_tratado['data'] = pd.to_datetime(df_tratado['data'], errors='coerce')
df_tratado['data_extracao'] = pd.to_datetime(df_tratado['data_extracao'],errors='coerce')

# As colunas 'data' e 'data_extracao' estavam armazenadas como texto. A conversão para o tipo datetime
# permite realizar operações temporais, como filtrar por ano ou mês.

df_tratado['ano'] = df_tratado['data'].dt.year
df_tratado['mes'] = df_tratado['data'].dt.month

# Foram extraídas as informações de ano e mês a partir da coluna 'data',
# criando novas colunas que facilitarão análises temporais nas próximas etapas.

df_tratado['hora_int'] = df_tratado['hora'].str[:2].astype(float)

# A coluna 'hora' estava no formato de texto "19:00:00.0000000". Foram extraídos apenas
# os dois primeiros caracteres para obter a hora inteira como valor numérico.
# Os 629 registros sem hora registrada receberam NaN automaticamente.

df_tratado = df_tratado.dropna(subset=['regiao'])

# A coluna 'regiao' apresentou apenas 1 valor ausente. A linha foi removida
# pois representa menos de 0,01% da base e não há como inferir a região correta.

df_tratado = df_tratado.drop(columns=['consorcio'])

# A coluna 'consorcio' foi removida por apresentar 72.766 valores ausentes,
# o equivalente a 97% dos registros. Com esse volume de dados faltantes,
# a coluna não oferece informação confiável para análise.

# As colunas 'longitude' e 'latitude' possuem 10.596 valores ausentes (14%).
# Optou-se por manter essas linhas, pois as demais informações do registro
# (tipo de acidente, vítimas, região) continuam válidas para análises não-geográficas.

# A coluna 'log2' possui 54.523 valores ausentes (72%). Esses nulos são esperados,
# pois a coluna representa a segunda rua de um cruzamento — acidentes em vias únicas
# naturalmente não possuem esse dado.

# A coluna 'hora' possui 629 valores ausentes (menos de 1% da base).
# Optou-se por manter os registros, pois o volume é insignificante
# e as demais informações dessas linhas permanecem úteis.

df_tratado['periodo_cod'] = df_tratado['noite_dia'].map({'DIA': 0, 'NOITE': 1})

# A coluna 'noite_dia' foi convertida para valores numéricos (DIA=0, NOITE=1),
# permitindo uso em cálculos como proporção de acidentes noturnos.

df_tratado['vitimas_graves'] = df_tratado['feridos_gr'] + df_tratado['mortes'] + df_tratado['morte_post']

# Foi criada a coluna 'vitimas_graves' somando feridos graves, mortes imediatas
# e mortes posteriores. Isso facilita a análise de severidade dos acidentes
# sem precisar somar múltiplas colunas em cada consulta.

df_tratado['teve_fatal'] = (df_tratado['fatais'] > 0).astype(int)

# Foi criada a coluna 'teve_fatal' com valor 1 quando houve ao menos uma vítima fatal
# e 0 caso contrário. Essa coluna permite calcular facilmente a proporção de
# acidentes com desfecho fatal na base.

print(df_tratado.shape)

# Após o tratamento, a base passou de 34 para 39 colunas (inclusão de ano, mes, hora_int,
# periodo_cod, vitimas_graves e teve_fatal, com remoção de consorcio) e de 75.176
# para 75.175 registros, devido à remoção da linha com região ausente.

print(df_tratado.isnull().sum())

# Os valores ausentes restantes estão concentrados nas colunas de localização geográfica
# e logradouros, cujos nulos foram mantidos intencionalmente conforme justificado acima.

print(df_tratado.head())

# Visualização das primeiras linhas da base tratada para confirmação das alterações realizadas.