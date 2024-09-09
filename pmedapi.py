from pymed import PubMed  # Import the PubMed class from the pymed module

# Initialize the PubMed object with a tool name and email address
pubmed = PubMed(tool="MyTool", email="sartajsingh8@gmail.com")

# Perform a query for articles related to "prebiotic" with a maximum of 100 results
results = pubmed.query("prebiotic", max_results=10)

# Process the results
for article in results:
    print(article.title)  # Print the title of the article
    print(article.keywords)  # Print the abstract of the article  
    print(article.conclusions)  # Print the conclusions of the article 