from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Remplacez par votre propre clé API NumVerify
NUMVERIFY_API_KEY = 'YOUR_API_KEY'
NUMVERIFY_API_URL = 'http://apilayer.net/api/validate'

def check_with_numverify(number):
    params = {
        'access_key': NUMVERIFY_API_KEY,
        'number': number,
        'format': 1
    }
    response = requests.get(NUMVERIFY_API_URL, params=params)
    return response.json()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_number', methods=['POST'])
def check_number():
    data = request.get_json()
    number = data.get('number')
    
    # Supprimer le "+" s'il est présent au début
    if number.startswith('+'):
        number = number[1:]  # Supprime le premier caractère (le "+")
    
    if not number or not number.isdigit():
        return jsonify({'error': 'Numéro invalide'}), 400
    
    numverify_response = check_with_numverify(number)
    
    if 'error' in numverify_response:
        return jsonify({'error': 'Erreur API NumVerify'}), 500
    
    # Construction de la réponse avec toutes les informations disponibles
    response_data = {
        'valid': numverify_response['valid'],
        'number': numverify_response['number'],
        'local_format': numverify_response['local_format'],
        'international_format': numverify_response['international_format'],
        'country_name': numverify_response['country_name'],
        'country_code': numverify_response['country_code'],
        'line_type': numverify_response['line_type']
        # Ajoutez d'autres champs si nécessaire
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
