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


def get_random_article_pageid():
    random_request = requests.get(url=URL, params=PARAMS)
    random_request_data = random_request.json()

    random_article = random_request_data["query"]["random"][0]

    return int(random_article['id'])


def get_article_text(pageid: int):
    h = html2text.HTML2Text()
    h.ignore_links = True

    page_params = {
        "action": "parse",
        "pageid": pageid,
        "format": "json"
    }

    page_request = requests.get(url=URL, params=page_params)
    page_contents = page_request.json()

    return h.handle(page_contents['parse']['text']['*'])


def get_random_article_text():
    return get_article_text(get_random_article_pageid())


if __name__ == "__main__":
    print(get_random_article_text())
