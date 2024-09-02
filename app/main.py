from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import os

# Define the URL and search topic
URL = "https://example-news-website.com"
SEARCH_TERM = "technology"

def setup_driver():
    """Set up the Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Remote(
        command_executor=os.getenv('SELENIUM_REMOTE_URL', 'http://selenium:4444/wd/hub'),
        options=options
    )
    return driver

def search_and_extract(driver):
    """Navigate to the website, search for the term, and extract headlines."""
    driver.get(URL)

    # Find the search input and enter the search term
    search_input = driver.find_element(By.NAME, "q")  # Adjust the selector as needed
    search_input.send_keys(SEARCH_TERM)
    search_input.send_keys(Keys.RETURN)

    # Extract article headlines and URLs
    headlines = driver.find_elements(By.XPATH, "//h3[@class='article-title']/a")  # Adjust the XPath as needed
    results = [(headline.text, headline.get_attribute('href')) for headline in headlines]
    return results

def save_results_to_csv(results):
    """Save extracted data to a CSV file."""
    output_file = "output/results.csv"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Headline", "URL"])
        writer.writerows(results)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    driver = setup_driver()
    try:
        results = search_and_extract(driver)
        save_results_to_csv(results)
    finally:
        driver.quit()
