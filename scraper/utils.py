import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser


def is_allowed_to_scrape(url):
    """
    Checks if scraping the given URL is allowed based on the site's robots.txt file.
    
    Args:
        url (str): The URL to check.
        
    Returns:
        bool: True if scraping is allowed, False otherwise.
    """
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
        for entry in rp.entries:
            print(entry)
        return rp.can_fetch("*", url)
    except:
        print(f"Couldn't retrieve or parse robots.txt for {robots_url}. Proceeding with caution.")
        return False  # Default to False if there's an issue with robots.txt

def fetch_content(url, selector={'tag': 'p', 'class_': ''}):
    """
    Fetches and parses content from the provided URL based on the HTML selector, if allowed by robots.txt.
    
    Args:
        url (str): The URL of the site to parse.
        selector (dict): Dictionary with tag and attributes to find the desired HTML elements.
                         Example: {'tag': 'h1', 'class_': 'entry-title'}
    
    Returns:
        list: A list of text content from the matched elements.
    """
    if not is_allowed_to_scrape(url):
        print(f"Scraping disallowed by robots.txt for {url}. Skipping...")
        return []

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for non-2xx responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(selector['tag'], class_=selector.get('class_'))
    return [element.get_text() for element in elements]
