import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv("../data/consumo_energia.csv")

# Cálculos
df["consumo_rede"] = df["consumo_kwh"] - df["geracao_solar_kwh"]
df["economia_percentual"] = (df["geracao_solar_kwh"] / df["consumo_kwh"]) * 100
df["co2_evitado"] = df["geracao_solar_kwh"] * 0.084  # fator ANEEL

# Gráfico 1 – Consumo vs Solar
plt.figure(figsize=(8,5))
plt.plot(df["dia"], df["consumo_kwh"], label="Consumo Total (kWh)")
plt.plot(df["dia"], df["geracao_solar_kwh"], label="Geração Solar (kWh)")
plt.legend()
plt.xlabel("Dia")
plt.ylabel("kWh")
plt.title("Consumo Total x Geração Solar")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../docs/grafico_consumo.png")
plt.close()

# Gráfico 2 – Economia percentual
plt.figure(figsize=(8,5))
plt.bar(df["dia"], df["economia_percentual"])
plt.xlabel("Dia")
plt.ylabel("Economia (%)")
plt.title("Economia de Energia com Uso de Painéis Solares")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../docs/grafico_solar.png")
plt.close()

# Resultado agregado
impacto_total = df[["geracao_solar_kwh", "co2_evitado"]].sum()
print("Energia solar total gerada (kWh):", impacto_total["geracao_solar_kwh"])
print("CO₂ evitado (kg):", impacto_total["co2_evitado"])
