from flask import Flask, request, jsonify, render_template
from scraper import scrape_shopify_data, extract_brand_name
from models import BrandContext
from competitor_finder import get_competitor_urls
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/get-insights', methods=['POST', 'GET'])
def get_insights():
    if request.method == 'POST':
        website_url = request.json.get('url')
    else:
        website_url = request.args.get('url')

    if not website_url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        result = scrape_shopify_data(website_url)
        result['website'] = website_url
        result['brand_name'] = extract_brand_name(website_url)
        validated = BrandContext(**result)
        return jsonify(validated.dict())
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Website not reachable'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)