import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

# Carica il file CSV con il delimitatore corretto
csv_path = 'PITTORI_csv.csv'  # Assicurati che il file sia nella stessa directory dello script
csv_data = pd.read_csv(csv_path, delimiter=';')
csv_data.columns = ['Pittore', 'Numero libro', 'Titoli libri']

# Funzione per trovare un pittore
def find_pittore(pittore_name):
    pittore_data = csv_data[csv_data['Pittore'].str.contains(pittore_name, case=False, na=False)]
    if not pittore_data.empty:
        results = []
        for _, row in pittore_data.iterrows():
            results.append(f"Del pittore {row['Pittore']} hai questi libri: {row['Numero libro']}")
        return "\n".join(results)
    else:
        return f"Pittore '{pittore_name}' non trovato."

# Definizione dell'interfaccia
class PittoriApp(App):
    def build(self):
        # Layout principale
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Campo di input per il nome del pittore
        self.input = TextInput(hint_text="Inserisci il nome del pittore", multiline=False, size_hint=(1, 0.2))
        self.layout.add_widget(self.input)
        
        # Etichetta per mostrare i risultati
        self.result_label = Label(text="", size_hint=(1, 0.6))
        self.layout.add_widget(self.result_label)
        
        # Bottone per avviare la ricerca
        self.search_button = Button(text="Cerca", size_hint=(1, 0.2))
        self.search_button.bind(on_press=self.on_search)
        self.layout.add_widget(self.search_button)
        
        return self.layout

    def on_search(self, instance):
        # Legge il nome dal campo di input
        pittore_name = self.input.text.strip()
        if pittore_name:
            # Cerca il pittore e aggiorna la label con i risultati
            result = find_pittore(pittore_name)
            self.result_label.text = result
        else:
            self.result_label.text = "Inserisci un nome valido!"

# Avvia l'app
if __name__ == "__main__":
    PittoriApp().run()
