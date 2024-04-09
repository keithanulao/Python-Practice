#Web Scrapper 
import time
import os


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define relevant class names (replace if necessary)
BBC_NEWS_WAIT_ELEMENT_CLASS = "gel-heading-scroll"
BBC_NEWS_TITLE_ELEMENT_CLASS = "gs-c-promo-heading__title"


def get_articles_with_selenium(url):
  """Uses Selenium to navigate a website and extract article titles.

  Args:
      url: The URL of the website to scrape.

  Returns:
      A list of strings containing the extracted article titles, or None if an error occurs.
  """
  try:
    # Replace with the actual path to your ChromeDriver
    driver = webdriver.Chrome("path/to/chromedriver")
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, BBC_NEWS_WAIT_ELEMENT_CLASS)))

    # Extract article titles
    articles = driver.find_elements(By.CLASS_NAME, BBC_NEWS_TITLE_ELEMENT_CLASS)
    titles = [article.text.strip() for article in articles]

    driver.quit()
    return titles
  except (TimeoutException, ConnectionError) as e:
    print(f"Error scraping articles: {e}")
    return None


# ... rest of the code (user_input_article, restart, main) with minor adjustments




def user_input_article():
    # Example usage
    url = "https://www.bbc.com/news"
    titles = get_articles_with_selenium(url)

    if titles:
        print("Article Titles:")
    for title in titles:
        print(title)
    else:
        print("No articles found.")


def restart():
    """Prompts user to restart the program."""
    while True:
        restart = input("\nPress (ENTER) to restart the program ").lower().replace(' ', '')
        if restart == "":
            print("\n***Restarting Program***")
            time.sleep(1)
            os.system("cls")
            break
        else:
            os.system("cls")
            print("**Invalid Input**")
            print("\nTry Again")
            time.sleep(2)
            os.system("cls")


def main():
   while True:
        user_input_article()
        restart()


if __name__ == "__main__":
    main()
