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
df_input = pd.DataFrame(dati, columns=["Giver", "Receiver1", "Receiver2"])
print(df_input)

for i in range(len(righe)):
    excluded_value = df_input.iloc[i]["Giver"]
    random_value = random_element_exclude(df_input.iloc[:, 0], excluded_value)
    df_input.at[i, 'Receiver1_new'] = random_value  # Assegna il valore in posizione i-esima
# assegno la nuova colonna di receiver1
df_input['Receiver1'] = df_input['Receiver1_new']

for i in range(len(righe)):
    excluded_value = df_input.iloc[i]["Receiver1_new"]
    random_value = random_element_exclude(df_input.iloc[:, 1], excluded_value)
    while random_value == df_input.iloc[i, 0]:
        excluded_value = df_input.iloc[i]["Receiver1_new"]
        random_value = random_element_exclude(df_input.iloc[:, 1], excluded_value)
    df_input.at[i, 'Receiver2_new'] = random_value  # Assegna il valore in posizione i-esima
# assegno la nuova colonna di receiver2 ed elimino le colonna extra

df_input['Receiver2'] = df_input['Receiver2_new']
df_input.drop('Receiver1_new', axis=1, inplace=True); df_input.drop('Receiver2_new', axis=1, inplace=True)

print(df_input)

#da implementare: che sia anche diverso da T0(solo se n righe maggiore di 3, altrimenti si spacca)