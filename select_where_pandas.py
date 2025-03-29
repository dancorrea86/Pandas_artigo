import pandas as pd

pessoas = pd.read_csv("Pessoas.csv", sep=";",header=0)

pessoas_brasil = pessoas[pessoas["Pais"] == 'Brazil']

print(pessoas_brasil)

