"""
========================================================================
ETL - ANÁLISE FINANCEIRA E PAGAMENTOS
Projeto Integrador - SENAC - Pessoa 6
========================================================================
TRANSFORM - Parte 1 (Inspeção Inicial dos Dados)
Objetivo: Carregar e entender a estrutura dos dados antes de limpar
========================================================================
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')
# O import de warnings é só pra remover alguns avisos que podem aparecer
# Serve exclusivamente pra limpeza e organização do output

# ============================================================================
# CONFIGURAÇÃO DE CAMINHOS (Relativo - funciona em qualquer computador)
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

# Caminhos para os dados
RAW_DATA_PATH = os.path.join(BASE_PATH, "data", "raw")
CLEANED_DATA_PATH = os.path.join(BASE_PATH, "data", "cleaned", "pessoa_6")

print("=" * 80)
print("ETAPA 1: CONFERÊNCIA DE CAMINHOS")
print("=" * 80, "\n")
# Mostrar os caminhos (para verificar)
print(f"─ Raiz do projeto: {BASE_PATH}")
print(f"─ Dados brutos: {RAW_DATA_PATH}")
print(f"─ Dados limpos: {CLEANED_DATA_PATH}\n")

# Configurações para visualização

# Mostrar todas as colunas, sem o corte no meio pra caber no terminal.
pd.set_option('display.max_columns', None)
# Largura automática.
pd.set_option('display.width', None)
# Limite de 50 caracteres por célula, padronizar a visualização.
pd.set_option('display.max_colwidth', 50)

print("=" * 80)
print("ETAPA 2: INSPEÇÃO INICIAL DOS DADOS FINANCEIROS")
print("=" * 80)
print(f"Início: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

