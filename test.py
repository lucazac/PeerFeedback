import pandas as pd  # Libreria per facilitare l'utilizzo di strutture dati
from function import random_element_exclude

# Leggere il file e processare i dati
with open("CoppiePrecedenti.txt", "r", encoding="utf-8") as file:
    righe = file.readlines()

# Creare una lista per memorizzare i dati separati
dati = []

for riga in righe:
    riga = riga.strip()  # Rimuove spazi bianchi iniziali e finali
    Giver, Receiver = riga.split(":")  # Divide il nome principale dai suoi amici
    Receiver = Receiver.replace(" ", "").split(",")  # Rimuove gli spazi e separa gli amici
    dati.append([Giver] + Receiver)  # Aggiunge i dati alla lista

# Creazione del DataFrame
df = pd.DataFrame(dati, columns=["Giver", "Receiver1", "Receiver2"])

print(df)
for i in range(len(righe)):
    excluded_value = df.iloc[i]["Giver"]
    print (excluded_value)