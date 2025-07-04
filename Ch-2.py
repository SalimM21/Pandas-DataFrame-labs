# Objectif : Filtrer un DataFrame pour ne conserver que les enregistrements répondant à une certaine condition.

# Chargez un DataFrame avec des données financières
import pandas as pd
df = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'Valeur': [100, 200, 150, 300]
})

# Filtrez le DataFrame pour ne conserver que les transactions d'un montant supérieur à 1000
df_filtered = df[df['Valeur'] > 1000]

# Affichez le DataFrame filtré
print(df_filtered)
# Note: In this example, no rows will be returned since all values are below 1000.
# If you want to see the DataFrame with all values, you can change the condition.
