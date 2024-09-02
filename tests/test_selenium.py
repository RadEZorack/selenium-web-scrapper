import pytest
from main import setup_driver, search_and_extract

def test_search_and_extract():
    driver = setup_driver()
    try:
        results = search_and_extract(driver)
        assert len(results) > 0, "No results found!"
        assert all(len(item) == 2 for item in results), "Results do not have the correct format!"
    finally:
        driver.quit()
