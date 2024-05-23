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

# Print the full article text
print(article_text)
