from randopedia import get_article_text


def test_article_text_returns_str():
    article_text = get_article_text(13541721)
    assert type(article_text) == str
