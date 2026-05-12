from bs4 import BeautifulSoup
import requests


def fetch_website_content_and_links(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title_and_content = get_website_content_from_soup(soup)
    return {
        "title": title_and_content["title"],
        "content": title_and_content["content"],
        "url": url,
        "links": get_links_from_soup(soup)
    }

def fetch_website_content(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title_and_content = get_website_content_from_soup(soup)
    return title_and_content["title"] + "\n" + title_and_content["content"]

def get_website_content_from_soup(soup: BeautifulSoup):
    title = soup.title.string if soup.title else "No title found"
    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    return {
        "title": title,
        "content": text[:2000]
    }


def get_links_from_soup(soup: BeautifulSoup):
    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]