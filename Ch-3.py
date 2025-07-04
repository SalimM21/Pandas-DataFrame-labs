# Objectif : Agréger des données pour obtenir des statistiques par groupe.

# Chargez un DataFrame contenant des informations sur les ventes
import pandas as pd
df = pd.DataFrame({
    'Vendeur': ['Alice', 'Bob', 'Alice', 'Bob', 'Alice'],
    'Montant': [100, 200, 150, 300, 250]
})

# Utilisez pandas.DataFrame.groupby() pour calculer le total des ventes par région

df_grouped = df.groupby('Vendeur')['Montant'].sum().reset_index()

# Affichez le DataFrame agrégé
print(df_grouped)

# Note: This will show the total sales amount for each vendor.