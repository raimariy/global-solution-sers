Entregantes
Ana Flávia Couto Chaves - RM: 566603
Raissa Marinho de Jesus Viana - RM: 568301

# GLOBAL SOLUTION – Simulação de Uso de Energia Solar (30 dias)

## 1. Introdução
A busca por ambientes de trabalho mais sustentáveis exige a adoção de tecnologias limpas e eficientes. A energia solar é uma alternativa real e acessível para reduzir os custos com eletricidade e diminuir o impacto ambiental.  
Este projeto apresenta uma **simulação de 30 dias** avaliando como a inclusão de painéis solares afeta o consumo energético de um ambiente corporativo.


## 2. Objetivo
Avaliar o impacto da energia solar no consumo total por meio de:

- Redução da dependência da rede elétrica  
- Economia estimada (%)  
- Redução de CO₂ emitido  
- Demonstração do potencial de energias renováveis no futuro do trabalho

## 3. Dados Utilizados
O arquivo `consumo_energia_30dias.csv` contém:

| Coluna              | Descrição                                        |
|---------------------|--------------------------------------------------|
| `dia`               | Dia da simulação                                 |
| `consumo_kwh`       | Consumo energético do dia                        |
| `geracao_solar_kwh` | Energia solar gerada no mesmo período            |

 
## 4. Metodologia da Simulação

Foram aplicadas quatro métricas principais:

### 1-Consumo da rede elétrica  

`consumo_rede = consumo_kwh - geracao_solar_kwh`

### 2-Economia percentual

`economia_percentual = (geracao_solar_kwh / consumo_kwh) * 100`

### 3-Redução de CO₂

Fator brasileiro de emissão: 0,084 kg CO₂ / kWh

`co2_evitado = geracao_solar_kwh * 0.084`

### 4-Gráficos

- Gráfico do consumo x geração solar
- Gráfico da economia percentual

## 5. Como Executar o Código

**Requisitos**

- Python 3.10+
- Bibliotecas:

pip install pandas matplotlib

▶️ Executando
cd src
python simulacao_energia_solar.py
