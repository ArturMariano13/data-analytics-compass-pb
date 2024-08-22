import pandas as pd

# Carregar o DataFrame
df = pd.read_csv('PALAS_OPERACOES_2024_01_corrigido.csv', delimiter=';')

"""# Exibir as primeiras linhas e os cabeçalhos das colunas
print(df.head())
print(df.columns)
"""

# Verificar se há valores não numéricos na coluna "Qtd Valores Apreendidos"
# Converta a coluna para numérico, forçando erros a serem NaN, e depois verifique se há NaNs
df['Qtd Valores Apreendidos'] = pd.to_numeric(df['Qtd Valores Apreendidos'], errors='coerce')
non_numeric_values = df[df['Qtd Valores Apreendidos'].isna()]

# Exibir as linhas com valores não numéricos
print(non_numeric_values['Qtd Valores Apreendidos'])
