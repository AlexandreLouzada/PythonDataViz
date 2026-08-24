import pandas as pd
import numpy as np
import json

# Configuração de semente para reprodutibilidade dos dados
np.random.seed(42)
num_registros = 1000

# 1. Gerando componentes do dataset
datas = pd.date_range(start='2026-01-01', periods=num_registros, freq='15min')
clientes = [f'C{i:03d}' for i in range(1, 101)]  # 100 clientes únicos
categorias = ['Eletrônicos', 'Moda', 'Casa', 'Livros', 'Esportes']
estados = ['SP', 'RJ', 'MG', 'RS', 'PR', 'BA', 'PE']
status_opcao = ['Concluído', 'Concluído', 'Concluído', 'Cancelado', 'Pendente']
sistemas_opcao = [
    '{"sistema": "iOS", "versao_app": "2.2"}',
    '{"sistema": "Android", "versao_app": "2.1"}',
    '{"sistema": "Web", "versao_app": "N/A"}'
]

# 2. Montando o dicionário de dados
dados = {
    'transacao_id': np.arange(1001, 1001 + num_registros),
    'data_hora': datas.strftime('%Y-%m-%d %H:%M:%S'),
    'cliente_id': np.random.choice(clientes, size=num_registros),
    'categoria': np.random.choice(categorias, size=num_registros, p=[0.25, 0.30, 0.20, 0.15, 0.10]),
    'valor_venda': np.round(np.random.exponential(scale=250, size=num_registros) + 20, 2),
    'estado': np.random.choice(estados, size=num_registros),
    'status': np.random.choice(status_opcao, size=num_registros),
    'detalhes_acesso': np.random.choice(sistemas_opcao, size=num_registros)
}

df_gerado = pd.DataFrame(dados)

# 3. Inserindo ruídos propositais (valores nulos em 'valor_venda' para treinar imputação)
indices_nulos = np.random.choice(df_gerado.index, size=40, replace=False)
df_gerado.loc[indices_nulos, 'valor_venda'] = np.nan

# 4. Salvando o arquivo físico na pasta local de trabalho
nome_arquivo = 'vendas.csv'
df_gerado.to_csv(nome_arquivo, index=False, sep=';', encoding='utf-8')

print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
print(f"Total de linhas: {df_gerado.shape[0]} | Total de colunas: {df_gerado.shape[1]}")