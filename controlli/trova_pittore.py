import pandas as pd

# Carica il file CSV con il delimitatore corretto
csv_path = 'PITTORI_csv.csv'  # Assicurati che il file sia nella stessa directory dello script
csv_data = pd.read_csv(csv_path, delimiter=';')

# Rinomina le colonne per chiarezza
csv_data.columns = ['Pittore', 'Numero libro', 'Titoli libri']

# Funzione per trovare un pittore
def find_pittore(pittore_name):
    # Cerca il nome del pittore (case-insensitive)
    pittore_data = csv_data[csv_data['Pittore'].str.contains(pittore_name, case=False, na=False)]
    if not pittore_data.empty:
        for _, row in pittore_data.iterrows():
            print(f"Del pittore {row['Pittore']} hai questi libri: {row['Numero libro']}")
    else:
        print(f"Pittore '{pittore_name}' non trovato.")
# Esempio di utilizzo
if __name__ == "__main__":
    pittore_name = input("Inserisci il nome del pittore: ")  # Input da tastiera
    find_pittore(pittore_name)