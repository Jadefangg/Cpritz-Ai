from pymed import PubMed  # PubMed library data
import json

# Initialize the PubMed object
pubmed = PubMed(tool="MyTool", email="sartajsingh8@gmail.com")

# Perform a query
results = pubmed.query("prebiotic", max_results=100)

# Process the results and store them in a list
article_data = []  # Storing queried data.
for article in results:
    article_data.append({
        "title": article.title,
        "keywords": article.keywords,
        "conclusion": article.conclusions,
        "publication_date": article.publication_date
    })

# Save article_data to a JSON file
with open('article_data.json', 'w') as json_file:
    json.dump(article_data, json_file, indent=4)

# Function to return the stored results
def results():
    with open('article_data.json', 'r') as json_file:
        return json.load(json_file)

results_data = results()

# Chatbot response function
def chatbot_response(user_input):
    response = "I couldn't find any articles related to your query."
    for article in results_data:
        if user_input.lower() in article["title"].lower() or \
           any(user_input.lower() in keyword.lower() for keyword in article["keywords"]) or \
           user_input.lower() in article["conclusion"].lower():
            response = f"Found an article: {article['title']}\nConclusion: {article['conclusion']}"
            break
    return response

# Chatbot interaction loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot_response(user_input))
