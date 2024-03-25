from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Fonction pour charger les données Velib
def load_velib_data():
    data = pd.read_csv("C:/Users/selsa/OneDrive/Documents/Velib/velib-pos.csv", delimiter=';')

    js_data = "[\n"
    for index, row in data.iterrows():
        js_data += f"    {{name: '{row['Nom de la station']}', latitude: {row['geo'].split(',')[0]}, longitude: {row['geo'].split(',')[1]}}},\n"
    js_data += "];\n"

    return js_data

# Route pour la page d'accueil
@app.route('/')
def index():
    velib_stations = load_velib_data()
    return render_template('map.html', v=velib_stations)

if __name__ == '__main__':
    app.run(debug=True)