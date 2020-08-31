from randopedia import get_random_article_pageid


def check_different_article_pageids_are_returned():
    counter = 0
    pageids = []
    while counter < 10:
        pageid = get_random_article_pageid()
        assert pageid not in pageids