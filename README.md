# GLOBAL SOLUTION – Simulação de Uso de Energia Solar Fotovoltaica On-Grid

## Integrantes
- Ana Flávia Couto Chaves – RM: 566603  
- Raissa Marinho de Jesus Viana – RM: 568301  

---

## Objetivo

Este projeto tem como objetivo simular a aplicação de um sistema de energia **solar fotovoltaica on-grid** em dois cenários diferentes:  
- Uma **residência (casa)**  
- Uma **empresa**

A proposta é analisar os impactos da geração de energia solar no:
- Consumo de energia elétrica
- Custo financeiro (economia na conta de luz)
- Redução da emissão de CO₂  

A solução está diretamente relacionada à sustentabilidade e ao futuro do trabalho, promovendo eficiência energética e redução de impactos ambientais.

---

## Dados Utilizados

Os dados utilizados neste projeto são simulados, com valores realistas de consumo de energia elétrica e geração de energia solar fotovoltaica. Esses dados foram criados com o objetivo de permitir a análise da viabilidade econômica e ambiental da aplicação de um sistema fotovoltaico on-grid em uma residência e em uma empresa.

Foram utilizados três arquivos no formato CSV:

- consumo_casa.csv
- consumo_empresa.csv
- geracao_solar.csv

**Arquivo:** consumo_casa.csv

Este arquivo contém os dados de consumo mensal de energia de uma residência.
| Coluna        | Descrição                        |
| ------------- | -------------------------------- |
| `Mes`         | Mês da simulação                 |
| `Consumo_kWh` | Consumo de energia da residência |

**Arquivo:** consumo_empresa.csv

Este arquivo contém os dados de consumo mensal de energia de uma empresa.
| Coluna        | Descrição                     |
| ------------- | ----------------------------- |
| `Mes`         | Mês da simulação              |
| `Consumo_kWh` | Consumo de energia da empresa |

**Arquivo:** geracao_solar.csv

Este arquivo contém os dados de geração mensal do sistema fotovoltaico.
| Coluna        | Descrição                                    |
| ------------- | -------------------------------------------- |
| `Mes`         | Mês da simulação                             |
| `Geracao_kWh` | Energia solar fotovoltaica gerada no período |


## Tipo de Sistema Utilizado

O sistema considerado na simulação é do tipo:

**Fotovoltaico On-Grid**

Nesse modelo:
- A energia solar é consumida instantaneamente.
- O excedente é injetado na rede da concessionária.
- Esse excedente gera **créditos energéticos**, que são utilizados nos períodos sem sol.
- Não há uso de baterias.

---

## Cenários Simulados

### 1. Casa
- Alta disponibilidade de área para instalação dos painéis.
- Capacidade de atender grande parte (ou até 100%) do consumo.
- Elevada economia financeira.
- Grande redução de CO₂.

### 2. Empresa
- Área limitada para instalação dos painéis.
- Cobertura fotovoltaica parcial (aproximadamente 25%).
- Economia relevante mesmo com geração parcial.
- Redução significativa de CO₂.

### Comparação dos Cenários: Casa x Empresa

A simulação foi realizada em dois cenários para mostrar como os resultados da energia solar fotovoltaica on-grid variam conforme o tipo de consumo.

Na residência, é mais comum alcançar até 100% de cobertura do consumo, pois a demanda é menor e a área disponível para os painéis geralmente é suficiente. Já na empresa, o consumo é mais elevado e a área para instalação pode ser limitada, resultando em uma geração parcial de energia, como ocorreu na simulação.

A escolha desses dois cenários permite comparar realidades diferentes e mostrar que, apesar das limitações, a energia solar continua sendo uma solução viável e sustentável.

---

## Como Executar o Código

**Baixar o repositório**
Você pode clonar o projeto com:

```bash
git clone <link_do_repositorio>
```

Ou baixar os arquivos manualmente pelo GitHub.

**Bibliotecas necessárias:**
pip install pandas numpy matplotlib seaborn

**Executando:**
cd src
python simulacao_de_uso_de_energias_renovaveis.py

Ou executar diretamente no Google Colab / Jupyter Notebook.

---

## Conexão com o Futuro do Trabalho

A transição para fontes de energia renováveis está diretamente ligada às transformações no mercado de trabalho. O avanço da energia solar fotovoltaica impulsiona a criação de novas profissões, como instaladores de sistemas solares, técnicos em manutenção, engenheiros especializados em energias renováveis, analistas de dados energéticos e desenvolvedores de soluções inteligentes para monitoramento de consumo.

Além disso, a digitalização dos sistemas energéticos, por meio de sensores, automação e análise de dados, exige profissionais cada vez mais capacitados em tecnologia, sustentabilidade e inovação. A integração entre programação, simulação computacional e energias renováveis demonstra como as competências do futuro envolvem não apenas conhecimento técnico, mas também a capacidade de propor soluções eficientes para problemas reais.

Nesse contexto, este projeto se conecta ao futuro do trabalho ao unir sustentabilidade, tecnologia e análise de dados, preparando os estudantes para atuar em um mercado cada vez mais voltado à eficiência energética, à responsabilidade ambiental e à inovação digital.

**Aplicação no Mercado de Trabalho**

- Expansão de empregos na área de energias renováveis
- Crescimento da demanda por profissionais em tecnologia e sustentabilidade
- Uso de programação e análise de dados para tomada de decisões
- Desenvolvimento de soluções inteligentes para eficiência energética
- Valorização de profissionais com visão socioambiental
