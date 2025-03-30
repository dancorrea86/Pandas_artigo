import pandas as pd

pessoas = pd.read_csv("Pessoas.csv", sep=";",header=0)

pessoas.loc[len(pessoas)] = ['Fulano', 'fulano@fulano.org', 'Brazil', 37]

pessoas = pessoas.loc[pessoas["Email"] != 'fulano@fulano.org']

# Alternativa
# pessoas = pessoas.drop(pessoas[pessoas.Email == 'fulano@fulano.org'].index)

print(pessoas)
