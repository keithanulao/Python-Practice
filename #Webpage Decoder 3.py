#Webpage Decoder 3

import os
import requests
from bs4 import BeautifulSoup

def get_article_text(url):
  """Fetches the article content from the given URL and extracts the full text."""

  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  # Find all article body paragraphs (adjust selector if needed)
  paragraphs = soup.select('article.article.main-content p')

  # Extract text from each paragraph
  article_text = '\n'.join([p.get_text(strip=True) for p in paragraphs])

  return article_text

# Replace with the actual URL of the article
article_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

article_text = get_article_text(article_url)

# Get user input for filename
filename = input("Enter a filename to save the article (e.g., article.txt): ")

# Create folder on Desktop (replace 'Windows' with your OS if different)
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Extracted_Articles')
if not os.path.exists(desktop_path):
  os.makedirs(desktop_path)  # Create folder if it doesn't exist

# Create full filepath with filename
filepath = os.path.join(desktop_path, filename)

# Open the file in write mode and save the text
with open(filepath, 'w') as file:
  file.write(article_text)

print(f"Article text saved to '{filepath}'.")
