import pandas as pd
import os

if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col= 0, parse_dates= True)
    df_receitas = pd.read_csv("df_receitas.csv", index_col= 0, parse_dates= True)
    df_despesas["Data"] = pd.to_datetime(df_despesas["Data"])
    df_receitas["Data"] = pd.to_datetime(df_receitas["Data"])
    df_receitas["Data"] = df_receitas["Data"].apply(lambda x: x.date())
    df_despesas["Data"] = df_despesas["Data"].apply(lambda x: x.date())

else: 
    data_structure = {"Valor": [],
                      "Efetuado": [],
                      "Fixo": [],
                      "Data": [],
                      "Categoria": [],
                      "Descrição": []}
    df_receitas = pd.DataFrame(data_structure).to_csv("df_receitas.csv")
    df_despesas = pd.DataFrame(data_structure).to_csv("df_despesas.csv")

if ("df_cat_despesas.csv" in os.listdir()) and ("df_cat_receitas.csv" in os.listdir()):
    df_cat_despesas = pd.read_csv("df_cat_despesas.csv", index_col= 0, parse_dates= True)
    df_cat_receitas = pd.read_csv("df_cat_receitas.csv", index_col= 0, parse_dates= True)
    cat_receita = df_cat_receitas.values.tolist()
    cat_despesa = df_cat_despesas.values.tolist()

else:
    cat_receita = {"Categoria": ["Salário", "Investimentos", "Comissão"]}
    cat_despesa = {"Categoria": ["Alimentação", "Transporte", "Lazer", "Moradia", "Saúde", "Educação", "Outros"]}

    df_despesas = pd.DataFrame(cat_despesa).to_csv("df_cat_despesas.csv")
    df_receitas = pd.DataFrame(cat_receita).to_csv("df_cat_receitas.csv")
