import requests
import json

# URL de tu endpoint
url = "https://us-central1-infra-core-428321-r6.cloudfunctions.net/get"

# Payload de ejemplo (ajusta los valores según lo que espere tu función)
payload = {
    "code": "Blastoise",     # Código o nombre de la carta
    "category": "Pokemon"       # Valor de categoría, por ejemplo para Pokémon
}

# Cabeceras (asegúrate de enviar JSON)
headers = {"Content-Type": "application/json"}

# Realiza la petición POST
response = requests.post(url, data=json.dumps(payload), headers=headers)

# Muestra el código de estado y la respuesta
print("Status Code:", response.status_code)
try:
    print("Response JSON:", response.json())
except Exception as e:
    print("Response content:", response.text)
