import config


def test_open_url(web_driver):
    web_driver.get(config.TEST_URL)
    assert web_driver.title, "page has no title"


def test_page_has_links(web_driver):
    web_driver.get(config.TEST_URL)
    links = web_driver.find_elements("tag name", "a")
    assert len(links) > 0
