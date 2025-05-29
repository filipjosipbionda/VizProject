import pandas as pd

# Učitaj originalni CSV
df = pd.read_csv("who_road_deaths.csv")

# Ukloni prvi red koji sadrži spolne oznake ("Both sexes", "Male", "Female")
df = df.iloc[1:].copy()

# Preimenuj stupce radi lakšeg pristupa
df.columns = [
    "Country", "Year",
    "Deaths_Both", "Deaths_Male", "Deaths_Female",
    "Rate_Both", "Rate_Male", "Rate_Female"
]

# Parsiraj broj poginulih – uzmi samo prvi broj prije razmaka ili zagrade
df["Deaths_Both"] = df["Deaths_Both"].str.extract(r"(\d+)").astype(int)
df["Deaths_Male"] = df["Deaths_Male"].str.extract(r"(\d+)").astype(int)
df["Deaths_Female"] = df["Deaths_Female"].str.extract(r"(\d+)").astype(int)

# Parsiraj stope smrtnosti – uzmi samo prvu brojčanu vrijednost (npr. 15.9 iz "15.9 [13.7-18.0]")
df["Rate_Both"] = df["Rate_Both"].str.extract(r"([\d.]+)").astype(float)
df["Rate_Male"] = df["Rate_Male"].str.extract(r"([\d.]+)").astype(float)
df["Rate_Female"] = df["Rate_Female"].str.extract(r"([\d.]+)").astype(float)

# Pretvori godinu u cijeli broj
df["Year"] = df["Year"].astype(int)

# Spremi očišćeni DataFrame u novi CSV
df.to_csv("road_deaths_full_cleaned.csv", index=False)

print("Podaci su uspješno očišćeni i spremljeni u 'road_deaths_full_cleaned.csv'.")
