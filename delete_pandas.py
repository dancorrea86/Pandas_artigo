import pandas as pd

pessoas = pd.read_csv("Pessoas.csv", sep=";",header=0)

pessoas_por_pais = pessoas.groupby("Pais").size()

print(pessoas_por_pais)