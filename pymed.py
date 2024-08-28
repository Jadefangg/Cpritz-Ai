from pymed import PubMed #PubMed library data

# Initialize the PubMed object
pubmed = PubMed(tool="MyTool", email="my@email.address")

# Perform a query
results = pubmed.query("nutrition", max_results=100)

# Process the results
for article in results:
    print(article.title)# Title of the article
    print(article.abstract) #
