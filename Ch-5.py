# Objectif : Résumer les données avec un tableau croisé dynamique

# Chargez un DataFrame contenant des données de ventes par produit et par région.
import pandas as pd
df = pd.DataFrame({
    'Produit': ['A', 'B', 'A', 'B', 'C'],
    'Région': ['Nord', 'Nord', 'Sud', 'Sud', 'Nord'],
    'Ventes': [100, 200, 150, 300, 250]
})

# Utilisez pandas.DataFrame.pivot_table() pour créer un tableau croisé dynamique qui montre la somme des ventes par produit et par région

df_pivot = df.pivot_table(values='Ventes', index='Produit', columns='Région', aggfunc='sum', fill_value=0)
print(df_pivot)


# Affichez le tableau croisé dynamique

# Note: This will show the total sales for each product in each region, with missing values filled with 0.
# Note: The pivot table will summarize the sales data, allowing for easy comparison of product sales    

