from randopedia import get_random_article_pageid
from time import sleep


def test_different_article_pageids_are_returned():
    counter = 0
    pageids = []
    while counter < 10:
        pageid = get_random_article_pageid()
        counter += 1
        assert pageid not in pageids