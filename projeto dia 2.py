import pandas as pd

tabela = pd.read_csv("telecom_users.csv")
tabela = tabela.drop("Unnamed: 0", axis=1)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
print(tabela["Churn"].value_counts())