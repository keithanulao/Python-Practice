#Web Scrapper 

import requests 
from bs4 import BeautifulSoup
import time
import os


def user_website_input():
    print("What website would you like to decode? ")
    url = input("\nPaste website here: ")
    return url


def decode(url):
    print("\nDecoding...")
    time.sleep(1)
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Look for articles in multiple sections (adjust class names based on website structure)
            sections = ["css-180t1jl", "css-okzqka", "css-183lgpq"]  # Example section class names (replace with actual class names)
            articles = []
            for section_class in sections:
                section_articles = soup.find_all("article", class_=section_class)
                articles.extend(section_articles)  # Combine articles from all sections

            # Extract titles
            for article in articles:
                title_element = article.find("h2")  # You can adjust the title tag if needed
                if title_element:
                    title = title_element.text.strip()
                    print(title)
        else:
            print(f"Failed to retrieve the {url} homepage (Status Code: {response.status_code})")

    except Exception as e:
        print("\n***ERROR***")
        print(f"An error occurred: {e}")


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
        os.system("cls")
        url = user_website_input()
        decode(url)
        restart()


if __name__ == "__main__":
  main()