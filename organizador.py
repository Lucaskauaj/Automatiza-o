import pandas as pd

df = pd.read_excel("Exemplo.xlsx")

df["Data"] = pd.to_datetime(df["Data"])

df["Mes"] = df["Data"].dt.to_period("M")

resumo = df.groupby(["Mes", "Vendedor"])["Valor"].sum().reset_index()

resumo.to_excel("resumo.xlsx", index=False)

print("Resumo salvo como resumo.xlsx")
