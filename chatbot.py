from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load article_data from the JSON file
try:
    with open('article_data.json', 'r') as json_file:
        article_data = json.load(json_file)
except FileNotFoundError:
    article_data = []

# Search function
def search_articles(query):
    results = []
    for article in article_data:
        if query.lower() in article["title"].lower() or query.lower() in article["conclusions"].lower():
            results.append(article)
    return results

# Chatbot endpoint
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('query')
    results = search_articles(user_input)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message": "No relevant articles found."})

if __name__ == '__main__':
    app.run(debug=True)