from bs4 import BeautifulSoup
import requests


def fetch_website_content_and_links(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return {
        "content": get_website_content_from_soup(soup),
        "links": get_links_from_soup(soup)
    }


def get_website_content_from_soup(soup: BeautifulSoup):
    title = soup.title.string if soup.title else "No title found"
    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    return (title + "\n\n" + text)[:2000]


def get_links_from_soup(soup: BeautifulSoup):
    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]