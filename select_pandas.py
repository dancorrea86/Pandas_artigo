import pandas as pd

pessoas = pd.read_csv("Pessoas.csv", sep=";",header=0)

pessoas_nome_pais = pessoas[["Nome", "Pais"]]