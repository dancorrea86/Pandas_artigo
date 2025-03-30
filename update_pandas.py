import pandas as pd

pessoas = pd.read_csv("Pessoas.csv", sep=";",header=0)

pessoas_brasil = pessoas.loc[pessoas['Pais'] == 'Brazil', 'Pais'] = 'Brasil'

pessoas_brasil = pessoas[pessoas["Pais"] == 'Brasil']

print(pessoas_brasil)