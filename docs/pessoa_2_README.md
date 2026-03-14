# Produtos e Categorias

**Responsável:** Pessoa 2

## 📊 Tabelas Principais

`products, product_category_name_translation, order_items`

## 🎯 Objetivos da Análise

- Categorias mais vendidas
- Preço médio por categoria
- Relação peso/volume e frete
- Produtos com melhores avaliações

## 📁 Estrutura

```
src/pessoa_2/
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
└── analysis/
    └── (scripts de análise)
```

## 🚀 Como Executar

```bash
# Extract
python src/pessoa_2/etl/extract.py

# Transform
python src/pessoa_2/etl/transform.py
```
