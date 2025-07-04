# Nettoyer un DataFrame en remplaçant les valeurs manquantes
import pandas as pd

# Chargez un DataFrame avec des données contenant des valeurs manquantes
data = {
    'A': [1, 2, None, 4]
}
df = pd.DataFrame(data)

# Utilisez pandas.DataFrame.fillna() pour remplacer les valeurs manquantes par la moyenne des colonnes
df.fillna(df.mean(), inplace=True)
# Affichez le DataFrame nettoyé
print(df)
