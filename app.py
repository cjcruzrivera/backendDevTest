from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/product/<int:product_id>/similar', methods=['GET'])
def get_similar_products(product_id):
    try:
        response = requests.get(f'https://api.example.com/products/{product_id}/similar')
        response.raise_for_status()
        
        similar_ids = response.json()

        similar_products = []
        for similar_id in similar_ids:
            similar_product_response = requests.get(f'https://api.example.com/products/{similar_id}')
            similar_product_response.raise_for_status()
            similar_products.append(similar_product_response.json())

        return jsonify({'similar_products': similar_products})
    
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(port=5000)
    
    
    