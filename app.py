from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/product/<string:product_id>/similar', methods=['GET'])
def get_similar_products(product_id):
    try:
        response = requests.get(f'http://simulado/product/{product_id}/similar')
        if response.status_code == 404:
            return jsonify({'error': 'Product not found'}), 404
        
        similar_ids = response.json()

        similar_products = []
        for similar_id in similar_ids:
            similar_product_response = requests.get(f'http://simulado/product/{similar_id}')
            if similar_product_response.status_code == 200:
                similar_products.append(similar_product_response.json())

        return jsonify(similar_products)
    
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
    
    