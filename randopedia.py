import requests
import html2text


URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "random",
    "rnlimit": "1",
    "rnnamespace": "0",
}


def get_random_article():
    h = html2text.HTML2Text()
    h.ignore_links = True

    random_request = requests.get(url=URL, params=PARAMS)
    random_request_data = random_request.json()

    random_article = random_request_data["query"]["random"][0]

    page_params = {
        "action": "parse",
        "pageid": random_article['id'],
        "format": "json"
    }
    page_request = requests.get(url=URL, params=page_params)
    page_contents = page_request.json()
    print(h.handle(page_contents['parse']['text']['*']))


if __name__ == "__main__":
    get_random_article()

