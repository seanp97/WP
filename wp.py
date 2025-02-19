import sys
import requests
from bs4 import BeautifulSoup

def get_css_links(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    css_links = [link['href'] for link in soup.find_all("link", rel="stylesheet") if 'href' in link.attrs]

    return css_links

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python wp.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    css_links = get_css_links(url)

    if not css_links:
        print("No CSS links found.")
    else:
        wp_links = [link for link in css_links if "wp-content" in link]
        if wp_links:
            print("The site is using Wordpress.")
        else:
            print("The site is not using Wordpress.")
