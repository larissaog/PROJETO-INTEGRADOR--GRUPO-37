# 📂 Estrutura Completa do Projeto

```
PROJETO-INTEGRADOR--GRUPO-37/
│
├── .gitignore                                 # Arquivos a ignorar no Git
├── README.md                                  # Documentação principal
├── requirements.txt                           # Dependências Python
│
├── data/                                      # 📊 DADOS
│   ├── raw/                                   # Dados originais (CSVs do Kaggle)
│   │   ├── olist_customers_dataset.csv
│   │   ├── olist_geolocation_dataset.csv
│   │   ├── olist_order_items_dataset.csv
│   │   ├── olist_order_payments_dataset.csv
│   │   ├── olist_order_reviews_dataset.csv
│   │   ├── olist_orders_dataset.csv
│   │   ├── olist_products_dataset.csv
│   │   ├── olist_sellers_dataset.csv
│   │   └── product_category_name_translation.csv
│   │
│   ├── cleaned/                               # Dados após limpeza
│   │   ├── pessoa_1/                          # Clientes
│   │   │   └── .gitkeep
│   │   ├── pessoa_2/                          # Produtos
│   │   │   └── .gitkeep
│   │   ├── pessoa_3/                          # Vendedores
│   │   │   └── .gitkeep
│   │   ├── pessoa_4/                          # Logística
│   │   │   └── .gitkeep
│   │   ├── pessoa_5/                          # Satisfação
│   │   │   └── .gitkeep
│   │   └── pessoa_6/                          # Financeiro
│   │       └── .gitkeep
│   │
│   ├── analysis/                              # Dados processados para análise
│   │   ├── pessoa_1/
│   │   │   └── .gitkeep
│   │   ├── pessoa_2/
│   │   │   └── .gitkeep
│   │   ├── pessoa_3/
│   │   │   └── .gitkeep
│   │   ├── pessoa_4/
│   │   │   └── .gitkeep
│   │   ├── pessoa_5/
│   │   │   └── .gitkeep
│   │   └── pessoa_6/
│   │       └── .gitkeep
│   │
│   └── integrated/                            # Dados integrados (final)
│       └── .gitkeep
│
├── src/                                       # 💻 CÓDIGO-FONTE
│   ├── shared/                                # Código compartilhado
│   │   └── __init__.py
│   │
│   ├── pessoa_1/                              # Cliente e Comportamento
│   │   ├── __init__.py
│   │   ├── etl/
│   │   │   └── __init__.py
│   │   └── analysis/
│   │       └── __init__.py
│   │
│   ├── pessoa_2/                              # Produtos e Categorias
│   │   ├── __init__.py
│   │   ├── etl/
│   │   │   └── __init__.py
│   │   └── analysis/
│   │       └── __init__.py
│   │
│   ├── pessoa_3/                              # Vendedores e Performance
│   │   ├── __init__.py
│   │   ├── etl/
│   │   │   └── __init__.py
│   │   └── analysis/
│   │       └── __init__.py
│   │
│   ├── pessoa_4/                              # Logística e Entregas
│   │   ├── __init__.py
│   │   ├── etl/
│   │   │   └── __init__.py
│   │   └── analysis/
│   │       └── __init__.py
│   │
│   ├── pessoa_5/                              # Satisfação e Avaliações
│   │   ├── __init__.py
│   │   ├── etl/
│   │   │   └── __init__.py
│   │   └── analysis/
│   │       └── __init__.py
│   │
│   └── pessoa_6/                              # Financeiro e Pagamentos
│       ├── __init__.py
│       ├── etl/
│       │   └── __init__.py
│       └── analysis/
│           └── __init__.py
│
├── notebooks/                                 # 📓 JUPYTER NOTEBOOKS
│   ├── pessoa_1_clientes/
│   │   └── .gitkeep
│   ├── pessoa_2_produtos/
│   │   └── .gitkeep
│   ├── pessoa_3_vendedores/
│   │   └── .gitkeep
│   ├── pessoa_4_logistica/
│   │   └── .gitkeep
│   ├── pessoa_5_satisfacao/
│   │   └── .gitkeep
│   ├── pessoa_6_financeiro/
│   │   └── .gitkeep
│   └── integracao/
│       └── .gitkeep
│
├── reports/                                   # 📊 RELATÓRIOS
│   ├── pessoa_1/
│   │   └── figures/
│   │       └── .gitkeep
│   ├── pessoa_2/
│   │   └── figures/
│   │       └── .gitkeep
│   ├── pessoa_3/
│   │   └── figures/
│   │       └── .gitkeep
│   ├── pessoa_4/
│   │   └── figures/
│   │       └── .gitkeep
│   ├── pessoa_5/
│   │   └── figures/
│   │       └── .gitkeep
│   ├── pessoa_6/
│   │   └── figures/
│   │       └── .gitkeep
│   └── final/
│       └── dashboard_integrado/
│           └── .gitkeep
│
├── app/                                       # 🎨 STREAMLIT DASHBOARD
│   ├── Home.py                                # Página inicial
│   ├── exemplos_graficos_financeiros.py       # ← Exemplos que criamos
│   └── pages/
│       ├── 1_👥_Clientes.py                   # ← Felipe
│       ├── 2_📦_Produtos.py                   # ← Amanda
│       ├── 3_🏪_Vendedores.py                 # ← Tomaz
│       ├── 4_🚚_Logística.py                  # ← Natalia
│       ├── 5_⭐_Satisfação.py                 # ← Larissa
│       ├── 6_💰_Financeiro.py                 # ← Lucas
│       └── 7_📊_Visão_Integrada.py
│
└── docs/                                      # 📚 DOCUMENTAÇÃO
    ├── README.md
    ├── pessoa_1_README.md
    ├── pessoa_2_README.md
    ├── pessoa_3_README.md
    ├── pessoa_4_README.md
    ├── pessoa_5_README.md
    └── pessoa_6_README.md                     
```

---

## 📊 Estatísticas da Estrutura

- **Total de pastas principais:** 6
- **Pastas por pessoa:** 6
- **Total de subpastas:** ~55
- **Arquivos .gitkeep:** ~24
- **Arquivos __init__.py:** ~18
- **Arquivos README:** 7

---

## 🎯 Legenda de Pastas

| Pasta | Descrição |
|-------|-----------|
| `data/raw/` | Dados originais do Kaggle (não modificar) |
| `data/cleaned/` | Dados limpos por cada pessoa |
| `data/analysis/` | Dados processados prontos para análise |
| `data/integrated/` | Dados finais consolidados |
| `src/*/etl/` | Scripts de Extract, Transform, Load |
| `src/*/analysis/` | Scripts de análise e métricas |
| `notebooks/` | Jupyter Notebooks para exploração |
| `reports/*/figures/` | Gráficos e visualizações |
| `app/` | Dashboard Streamlit |
| `docs/` | Documentação do projeto |

---

**Criado em:** 2026
**Projeto:** Integrador SENAC - Grupo 37  
**Membros do Grupo:** 
- **Felipe Mayer** - Pessoa 1
- **Amanda** - Pessoa 2
- **Tomaz Marinho** - Pessoa 3
- **Natália** - Pessoa 4
- **Larissa** - Pessoa 5
- **Lucas** - Pessoa 6
**Dataset:** Brazilian E-Commerce (Olist)
