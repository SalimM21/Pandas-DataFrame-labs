# Objectif : Fusionner deux DataFrames sur une clé commune

# Chargez deux DataFrames : l'un contenant des informations sur les clients, l'autre sur les commandes.

import pandas as pd
import numpy as np

# DataFrame des clients
df_clients = pd.DataFrame({
    'ClientID': [1, 2, 3, 4],
    'Nom': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
})
# DataFrame des commandes
df_commandes = pd.DataFrame({
    'CommandeID': [101, 102, 103, 104],
    'ClientID': [1, 2, 1, 3],
    'Montant': [250.0, 150.0, 300.0, 200.0]
})

# Fusionnez les DataFrames sur la colonne customer_id en utilisant pandas.DataFrame.merge()

df_fusion = pd.merge(df_clients, df_commandes, on='ClientID', how='inner', validate='one_to_many')

# Affichez le DataFrame fusionné
print(df_fusion)

# Note: This will show the merged DataFrame with customer details and their corresponding orders.