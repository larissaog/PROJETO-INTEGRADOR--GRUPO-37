# ========================================================================
# ETL - ANÁLISE FINANCEIRA E PAGAMENTOS
# Projeto Integrador - SENAC - Pessoa 6
# ========================================================================
# TRANSFORM - (Inspeção Inicial dos Dados)
# Objetivo: Carregar e entender a estrutura dos dados antes de limpar
# ========================================================================

import pandas as pd
import numpy as np
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')
# O import de warnings é só pra remover alguns avisos que podem aparecer
# Serve exclusivamente pra limpeza e organização do output

# ============================================================================
# CONFIGURAÇÃO DE CAMINHOS
# ============================================================================

# Descobre automaticamente a raiz do projeto
# Usando as funçõs OS pra garantir compatibilidade entre sistemas operacionais

# Pega o arquivo atual
arquivo_atual = os.path.abspath(__file__)

# Sobe 3 níveis para chegar na RAIZ
pasta_etl = os.path.dirname(arquivo_atual)
pasta_pessoa6 = os.path.dirname(pasta_etl)
pasta_src = os.path.dirname(pasta_pessoa6)
BASE_PATH = os.path.dirname(pasta_src)

# Definindo os caminhos para input e output dos dados
RAW_DATA_PATH = os.path.join(BASE_PATH, "data", "raw")
CLEANED_DATA_PATH = os.path.join(BASE_PATH, "data", "cleaned", "pessoa_6")

print("=" * 80)
print("ETAPA 1: CONFERÊNCIA DE CAMINHOS")
print("=" * 80, "\n")
# Mostrar os caminhos (para verificar)
print(f"─ Raiz do projeto: {BASE_PATH}")
print(f"─ Dados brutos: {RAW_DATA_PATH}")
print(f"─ Dados limpos: {CLEANED_DATA_PATH}\n")

# ============================================================================
# CONFIGURAÇÃO DA VISUALIZAÇÃO DE DADOS
# ============================================================================

# Mostrar todas as colunas, sem o corte no meio pra caber no terminal.
pd.set_option('display.max_columns', None)
# Largura automática.
pd.set_option('display.width', None)
# Limite de caracteres por célula, padronizar a visualização.
pd.set_option('display.max_colwidth', 15)

# ============================================================================
# CARREGAMENTO DOS DADOS
# ============================================================================

# Carregando a tabela de pagamentos
df_payments = pd.read_csv(os.path.join(RAW_DATA_PATH, "olist_order_payments_dataset.csv"))

# Carregando a tabela de itens de pedido
df_order_items = pd.read_csv(os.path.join(RAW_DATA_PATH, "olist_order_items_dataset.csv"))

# Carregando a tabela de pedidos
df_orders = pd.read_csv(os.path.join(RAW_DATA_PATH, "olist_orders_dataset.csv"))

# ============================================================================
# VISUALIZANDO OS NOSSOS DADOS
# ============================================================================

print("=" * 80)
print("ETAPA 2: INSPEÇÃO INICIAL DOS DADOS FINANCEIROS")
print("=" * 80)
print(f"Início: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

print(f"   # {len(df_payments):,} registros | {len(df_payments.columns)} colunas")
print(f"   # {len(df_order_items):,} registros | {len(df_order_items.columns)} colunas")
print(f"   # {len(df_orders):,} registros | {len(df_orders.columns)} colunas", "\n")

# ============================================================================
# ANÁLISE DE VALORES NULOS
# ============================================================================

def analisar_nulos(df, nome_tabela):
    nulos = df.isnull().sum()
    total_linhas = len(df)
    percentual = (nulos / total_linhas * 100).round(2)
    
    # Loop pra conferir todas as colunas
    for coluna in df.columns:
        contagem_nulos = nulos[coluna]
        perc_nulos = percentual[coluna]
        print(f"Coluna: {coluna} - Total de valores nulos: {contagem_nulos} - Percentual: {perc_nulos}%")

# ============================================================================
# ANÁLISE DO DATAFRAME - payments
# ============================================================================

print("=" * 80)
print("ETAPA 2.1: ANÁLISE DO DATAFRAME - payments")
print("=" * 80)
# O Shape é pra gerar a tupla dos dados do nosso dataset.
# O 0 são as linhas, o 1 são as colunas.
print(f"Dimensões da tabela: {df_payments.shape[0]:,} linhas x {df_payments.shape[1]} colunas", "\n")
analisar_nulos(df_payments, "payments")
print("\n" , "Colunas e tipos de dados:")
print("-" * 80)
print(df_payments.dtypes, "\n")
print("\n", "Primeiras cinco linhas:")
print("-" * 80)
# O head() automaticamente puxa 5 linhas
print(df_payments.head())
print()

# ============================================================================
# ANÁLISE DO DATAFRAME - order_items
# ============================================================================

print("=" * 80)
print("ETAPA 2.2: ANÁLISE DO DATAFRAME - order_items")
print("=" * 80)
print(f"Dimensões da tabela: {df_order_items.shape[0]:,} linhas x {df_order_items.shape[1]} colunas\n")
analisar_nulos(df_order_items, "order_items")
print("\n" , "Colunas e tipos de dados:")
print("-" * 80)
print(df_order_items.dtypes, "\n")
print("\n", "Primeiras cinco linhas:")
print("-" * 80)
# O head() automaticamente puxa 5 linhas
print(df_order_items.head())
print()

# ============================================================================
# ANÁLISE DO DATAFRAME - orders
# ============================================================================

print("=" * 80)
print("ETAPA 2.3: ANÁLISE DO DATAFRAME - orders")
print("=" * 80)
print(f"Dimensões da tabela: {df_orders.shape[0]:,} linhas x {df_orders.shape[1]} colunas\n")
analisar_nulos(df_orders, "orders")
print("\n" , "Colunas e tipos de dados:")
print("-" * 80)
print(df_orders.dtypes, "\n")
print("\n", "Primeiras cinco linhas:")
print("-" * 80)
# O head() automaticamente puxa 5 linhas
print(df_orders.head())
print()

