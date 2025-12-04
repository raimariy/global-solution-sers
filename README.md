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
Este arquivo contém os dados de consumo mensal de energia elétrica de uma residência.
| Coluna        | Descrição                        |
| ------------- | -------------------------------- |
| `Mes`         | Mês da simulação                 |
| `Consumo_kWh` | Consumo de energia da residência |

**Arquivo:** consumo_empresa.csv
Este arquivo contém os dados de consumo mensal de energia elétrica de uma empresa.
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

## Como Executar o Código

**Requisitos**

- Python 3.10+
- Bibliotecas:

pip install pandas matplotlib

**Executando**
cd src
python simulacao_energia_solar.py
