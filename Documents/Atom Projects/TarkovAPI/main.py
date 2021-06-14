import requests
import json
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# Working Api Link
# https://tarkov-api.ijos.es/api/items/ammunitions/7.62x25?rapidapi-key=2aff1c40c0msha0892173f7c583ep1ffadfjsn136ee117470a

# /GETAMMO
@app.route('/getammo')
def ammo_type():
    # Ammon 7.62 x 25
    url = "https://escape-from-tarkov.p.rapidapi.com/items/ammunitions"

    headers = {
        'x-rapidapi-key': "2aff1c40c0msha0892173f7c583ep1ffadfjsn136ee117470a",
        'x-rapidapi-host': "escape-from-tarkov.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    print(response.status_code) #expected 200
    content = response.text
    y = json.loads(content) #load json as object
    jsonformatted_str = json.dumps(y, indent=2)

    return jsonformatted_str
