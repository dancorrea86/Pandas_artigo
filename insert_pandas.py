import pandas as pd

pessoas = pd.read_csv("Pessoas.csv", sep=";",header=0)

print(f"\nQuantidade de linhas no DataFrame: {len(pessoas)}\n\n")

pessoas.loc[len(pessoas)] = ['Fulano', 'fulano@fulano.org', 'Brazil', 37]

print(pessoas)