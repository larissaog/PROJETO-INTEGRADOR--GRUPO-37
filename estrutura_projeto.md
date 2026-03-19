# 📂 Estrutura Completa do Projeto

**Projeto Integrador - SENAC - Grupo 37**  
**Dataset:** Brazilian E-Commerce Public Dataset by Olist  
**Abordagem:** Híbrida (Notebooks + Scripts + Dashboard)

---

## 🎯 Estrutura Simplificada

```
PROJETO-INTEGRADOR--GRUPO-37/
│
├── .gitignore                                 # Arquivos a ignorar no Git
├── README.md                                  # Documentação principal do projeto
├── requirements.txt                           # Dependências Python
│
├── data/                                      # 📊 DADOS
│   ├── raw/                                   # Dados originais do Kaggle (não modificar)
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
│   └── cleaned/                               # Dados após limpeza (por pessoa)
│       ├── pessoa_1/
│       ├── pessoa_2/
│       ├── pessoa_3/
│       ├── pessoa_4/
│       ├── pessoa_5/
│       └── pessoa_6/
│
├── src/                                       # 💻 SCRIPTS PYTHON (automação)
│   ├── pessoa_1/
│   │   ├── inspecionar_dados.py
│   │   └── (scripts de automação)
│   │
│   ├── pessoa_2/
│   │   ├── inspecionar_dados.py
│   │   └── (scripts de automação)
│   │
│   ├── pessoa_3/
│   │   ├── inspecionar_dados.py
│   │   └── (scripts de automação)
│   │
│   ├── pessoa_4/
│   │   ├── inspecionar_dados.py
│   │   └── (scripts de automação)
│   │
│   ├── pessoa_5/
│   │   ├── inspecionar_dados.py
│   │   └── (scripts de automação)
│   │
│   └── pessoa_6/
│       ├── inspecionar_dados_financeiros.py
│       └── (scripts de automação)
│
├── notebooks/                                 # 📓 JUPYTER NOTEBOOKS (trabalho principal)
│   ├── pessoa_1_clientes/
│   │   ├── 01_inspecao_inicial.ipynb
│   │   ├── 02_limpeza_dados.ipynb
│   │   ├── 03_analise_*.ipynb
│   │   └── (notebooks de análise)
│   │
│   ├── pessoa_2_produtos/
│   │   ├── 01_inspecao_inicial.ipynb
│   │   ├── 02_limpeza_dados.ipynb
│   │   ├── 03_analise_*.ipynb
│   │   └── (notebooks de análise)
│   │
│   ├── pessoa_3_vendedores/
│   │   ├── 01_inspecao_inicial.ipynb
│   │   ├── 02_limpeza_dados.ipynb
│   │   ├── 03_analise_*.ipynb
│   │   └── (notebooks de análise)
│   │
│   ├── pessoa_4_logistica/
│   │   ├── 01_inspecao_inicial.ipynb
│   │   ├── 02_limpeza_dados.ipynb
│   │   ├── 03_analise_*.ipynb
│   │   └── (notebooks de análise)
│   │
│   ├── pessoa_5_satisfacao/
│   │   ├── 01_inspecao_inicial.ipynb
│   │   ├── 02_limpeza_dados.ipynb
│   │   ├── 03_analise_*.ipynb
│   │   └── (notebooks de análise)
│   │
│   └── pessoa_6_financeiro/
│       ├── 01_inspecao_inicial.ipynb
│       ├── 02_limpeza_dados.ipynb
│       ├── 03_analise_*.ipynb
│       └── (notebooks de análise)
│
├── reports/                                   # 📊 RELATÓRIOS E VISUALIZAÇÕES
│   ├── pessoa_1/
│   │   └── figures/                           # Gráficos salvos (PNG, PDF)
│   ├── pessoa_2/
│   │   └── figures/
│   ├── pessoa_3/
│   │   └── figures/
│   ├── pessoa_4/
│   │   └── figures/
│   ├── pessoa_5/
│   │   └── figures/
│   └── pessoa_6/
│       └── figures/
│
├── app/                                       # 🎨 STREAMLIT DASHBOARD
│   ├── Home.py                                # Página inicial do dashboard
│   └── pages/
│       ├── 1_👥_Clientes.py
│       ├── 2_📦_Produtos.py
│       ├── 3_🏪_Vendedores.py
│       ├── 4_🚚_Logística.py
│       ├── 5_⭐_Satisfação.py
│       └── 6_💰_Financeiro.py
│
└── docs/                                      # 📚 DOCUMENTAÇÃO
    ├── README.md                              # Documentação geral
    ├── pessoa_1_README.md
    ├── pessoa_2_README.md
    ├── pessoa_3_README.md
    ├── pessoa_4_README.md
    ├── pessoa_5_README.md
    └── pessoa_6_README.md
```

---

## 🎯 Legenda de Pastas

| Pasta | Descrição | Conteúdo | Quem Modifica |
|-------|-----------|----------|---------------|
| **data/raw/** | Dados originais do Kaggle | CSVs imutáveis | ❌ Ninguém (somente leitura) |
| **data/cleaned/** | Dados após limpeza | CSVs tratados por pessoa | ✅ Cada pessoa (saída dos notebooks) |
| **src/** | Scripts Python | Scripts de automação/utilitários | ✅ Cada pessoa (opcional) |
| **notebooks/** | Jupyter Notebooks | Exploração, limpeza e análise | ✅ Cada pessoa (trabalho principal) |
| **reports/figures/** | Gráficos salvos | PNG, PDF, SVG | ✅ Cada pessoa (saída dos notebooks) |
| **app/** | Dashboard Streamlit | Interface web interativa | ✅ Cada pessoa (visualização final) |
| **docs/** | Documentação | READMEs, metodologia | ✅ Cada pessoa |

---

## 📂 Organização por Tipo de Conteúdo

### **📊 DADOS**
```
data/
├── raw/              → Dados originais (imutáveis)
└── cleaned/          → Dados limpos (output dos notebooks)
```

**Regra:** 
- ❌ **NUNCA** modificar `data/raw/`
- ✅ Salvar dados limpos em `data/cleaned/pessoa_X/`

---

### **💻 CÓDIGO**

#### **Scripts Python (src/)**
```
src/pessoa_X/
└── *.py              → Scripts de automação (opcional)
```

**Uso:** 
- Scripts que rodam automaticamente
- Funções reutilizáveis
- Processos batch

**Exemplo:**
- Inspeção inicial automatizada
- Validação de dados
- ETL agendado

---

#### **Notebooks Jupyter (notebooks/)**
```
notebooks/pessoa_X/
├── 01_*.ipynb        → Inspeção
├── 02_*.ipynb        → Limpeza
└── 03+_*.ipynb       → Análises específicas
```

**Uso:** 
- ✅ **Trabalho principal aqui!**
- Exploração interativa
- Limpeza de dados
- Análises e visualizações
- Testes de código

**Vantagens:**
- Vê resultado de cada célula
- Documenta com Markdown
- Combina código + texto + gráficos
- Ideal para aprendizado

---

### **📊 SAÍDAS**

#### **Dados Limpos (data/cleaned/)**
```
data/cleaned/pessoa_X/
├── tabela1_clean.csv
├── tabela2_clean.csv
└── dados_integrados.csv
```

**Gerado por:** Notebooks de limpeza  
**Usado por:** Notebooks de análise + Dashboard Streamlit

---

#### **Gráficos (reports/figures/)**
```
reports/pessoa_X/figures/
├── grafico1.png
├── grafico2.pdf
└── visualizacao.svg
```

**Gerado por:** Notebooks de análise  
**Usado por:** Relatório final, apresentações

---

### **🎨 VISUALIZAÇÃO**

#### **Dashboard Streamlit (app/)**
```
app/
├── Home.py           → Página inicial
└── pages/
    └── X_*.py        → Dashboard de cada pessoa
```

**Usa:** 
- CSVs limpos de `data/cleaned/`
- Importa funções de `src/` (se necessário)

**Gera:**
- Interface web interativa
- Gráficos dinâmicos
- KPIs e métricas

---

### **📚 DOCUMENTAÇÃO**

#### **READMEs (docs/)**
```
docs/
├── README.md         → Geral do projeto
└── pessoa_X_README.md → Específico de cada área
```

**Contém:**
- Metodologia
- Decisões técnicas
- Insights principais
- Instruções de uso

---

## 🔄 Fluxo de Trabalho Típico

### **Fase 1: Inspeção Inicial** 🔍

**Ferramentas:** Jupyter Notebook  
**Onde:** `notebooks/pessoa_X/01_inspecao_inicial.ipynb`

**Atividades:**
1. Carregar dados brutos de `data/raw/`
2. Explorar estrutura (colunas, tipos, dimensões)
3. Verificar valores nulos
4. Analisar estatísticas descritivas
5. Identificar problemas nos dados

**Output:**
- Entendimento dos dados
- Lista de problemas encontrados
- Plano de limpeza

---

### **Fase 2: Limpeza de Dados** 🧹

**Ferramentas:** Jupyter Notebook  
**Onde:** `notebooks/pessoa_X/02_limpeza_dados.ipynb`

**Atividades:**
1. Carregar dados brutos de `data/raw/`
2. Tratar valores nulos
3. Converter tipos de dados
4. Remover duplicados
5. Padronizar dados categóricos
6. Validar dados limpos
7. **SALVAR** em `data/cleaned/pessoa_X/`

**Output:**
- CSVs limpos em `data/cleaned/pessoa_X/*.csv`

---

### **Fase 3: Análises Específicas** 📊

**Ferramentas:** Jupyter Notebook  
**Onde:** `notebooks/pessoa_X/03_analise_especifica.ipynb`

**Atividades:**
1. **Carregar** dados limpos de `data/cleaned/pessoa_X/`
2. Realizar cálculos e agregações
3. Gerar insights
4. Criar visualizações
5. **Salvar gráficos** em `reports/pessoa_X/figures/`

**Output:**
- Insights e métricas
- Gráficos salvos (PNG, PDF)
- Análises documentadas

---

### **Fase 4: Dashboard Interativo** 🎨

**Ferramentas:** Streamlit  
**Onde:** `app/pages/X_*.py`

**Atividades:**
1. **Carregar** dados limpos de `data/cleaned/pessoa_X/`
2. Criar visualizações interativas
3. Adicionar filtros e controles
4. Apresentar KPIs
5. Documentar insights

**Output:**
- Dashboard web interativo
- Apresentação final

---

### **Fase 5: Documentação** 📚

**Ferramentas:** Markdown  
**Onde:** `docs/pessoa_X_README.md`

**Atividades:**
1. Documentar metodologia
2. Explicar decisões técnicas
3. Registrar insights principais
4. Instruções de uso

**Output:**
- Documentação completa
- Relatório técnico

---

## 🔀 Fluxo de Dados (Diagrama)

```
┌─────────────────┐
│  data/raw/      │ ← Dados originais (Kaggle)
│  *.csv          │
└────────┬────────┘
         │
         ↓ Lê (somente leitura)
┌─────────────────────────────────┐
│  notebooks/pessoa_X/            │
│  01_inspecao_inicial.ipynb      │ ← Explora
└─────────────────────────────────┘
         │
         ↓ Lê (somente leitura)
┌─────────────────────────────────┐
│  notebooks/pessoa_X/            │
│  02_limpeza_dados.ipynb         │ ← Limpa
└────────┬────────────────────────┘
         │
         ↓ Salva
┌─────────────────┐
│  data/cleaned/  │ ← CSVs limpos
│  pessoa_X/      │
└────────┬────────┘
         │
         ├──────────────────────────┐
         │                          │
         ↓ Lê                       ↓ Lê
┌──────────────────┐      ┌─────────────────┐
│  notebooks/      │      │  app/pages/     │
│  03_analise*.ipynb│      │  X_*.py         │
└────────┬─────────┘      └─────────────────┘
         │                         ↓
         ↓ Salva            Dashboard Web
┌──────────────────┐
│  reports/        │
│  pessoa_X/       │
│  figures/        │
└──────────────────┘
```

---

## 📝 Convenções e Boas Práticas

### **Nomenclatura de Arquivos**

#### **Notebooks:**
- `01_`, `02_`, `03_` → Ordem de execução
- Nomes descritivos em minúsculas
- Exemplo: `01_inspecao_inicial.ipynb`

#### **CSVs Limpos:**
- Nome original + `_clean`
- Exemplo: `payments_clean.csv`

#### **Gráficos:**
- Nome descritivo do conteúdo
- Exemplo: `receita_mensal.png`

---

### **Organização de Notebooks**

**Estrutura recomendada:**
```
# Célula 1: Markdown - Título e Descrição
# Célula 2: Código - Imports
# Célula 3: Código - Configurações
# Célula 4: Código - Carregamento de Dados
# Célula 5: Markdown - Seção de Análise
# Célula 6: Código - Análise
# Célula 7: Código - Visualização
# Célula 8: Markdown - Conclusões
```

---

### **Caminhos Relativos**

**Sempre use caminhos relativos:**
```python
# ✅ BOM (funciona em qualquer computador)
df = pd.read_csv('../../data/raw/arquivo.csv')

# ❌ RUIM (só funciona no seu computador)
df = pd.read_csv('C:/Usuário/Fulano/...')
```

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
