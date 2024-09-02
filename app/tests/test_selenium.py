import pytest

from ..main import setup_driver, scrape_hacker_news

def test_scrape_hacker_news():
    driver = setup_driver()
    try:
        results = scrape_hacker_news(driver)
        assert len(results) > 0, "No results found!"
        assert all(len(item) == 2 for item in results), "Results do not have the correct format!"
    finally:
        driver.quit()
