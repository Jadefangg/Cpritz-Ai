from pymed import PubMed #PubMed library data
import json
# Initialize the PubMed object
pubmed = PubMed(tool="MyTool", email="sartajsingh8@gmail.com")

# Perform a query
results = pubmed.query("prebiotic", max_results=100)

# Process the results
for article in results:
    print(article.title)# Title of the article
    print(article.keywords) 
    print(article.publication_date)
    
    print(article.conclusions)
    

#installed pymed

article_data = [] #storing queried data.
for article in results:
    article_data.append({
        "title": article.title,
        "keywords": article.keywords,
        "conclusions": article.conclusions,
    })

# Save article_data to a JSON file
with open('article_data.json', 'w') as json_file:
    json.dump(article_data, json_file, indent=4)