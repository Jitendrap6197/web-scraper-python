import requests
from bs4 import BeautifulSoup
def scrape_website(url):

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        titles = soup.find_all('h2')
        
        for index, title in enumerate(titles, start=1):
            print(f"{index}. {title.get_text(strip=True)}")
    else:
        print("Failed to retrieve the page")

if __name__ == "__main__":
    website_url = "https://www.geeksforgeeks.org"  
    scrape_website(website_url)
