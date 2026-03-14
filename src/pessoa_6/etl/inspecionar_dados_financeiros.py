"""
========================================================================
ETL - ANÁLISE FINANCEIRA E PAGAMENTOS
Projeto Integrador - SENAC - Pessoa 6
========================================================================
Etapa: TRANSFORM - Parte 1 (Inspeção Inicial dos Dados)
Objetivo: Carregar e entender a estrutura dos dados antes de limpar
========================================================================
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')

# O import de warnings é só pra remover alguns avisos que podem aparecer.
# Serve exclusivamente pra limpeza e organização do output.

# Configurações para visualização

# Mostrar todas as colunas, sem o corte no meio pra caber no terminal.
pd.set_option('display.max_columns', None)
# Largura automática.
pd.set_option('display.width', None)
# Limite de 50 caracteres por célula, padronizar a visualização.
pd.set_option('display.max_colwidth', 50)

