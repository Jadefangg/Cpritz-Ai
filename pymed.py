from pymed import PubMed #PubMed library data

# Initialize the PubMed object
pubmed = PubMed(tool="MyTool", email="sartajsingh8@gmail.com")

# Perform a query
results = pubmed.query("prebiotic", max_results=100)

# Process the results
for article in results:
    print(article.title)# Title of the article
    print(article.abstract) #
#installed pymed pip