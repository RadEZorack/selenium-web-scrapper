from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import os

# Define the URL to scrape
URL = "https://news.ycombinator.com/"

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

def scrape_hacker_news(driver):
    """Scrape Hacker News for story titles and URLs."""
    driver.get(URL)

    # Find the story titles and URLs
    stories = driver.find_elements(By.CLASS_NAME, "titleline")
    results = [(story.text, story.find_element(By.TAG_NAME, "a").get_attribute('href')) for story in stories]
    return results

def save_results_to_csv(results):
    """Save extracted data to a CSV file."""
    output_file = "output/results.csv"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "URL"])
        writer.writerows(results)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    driver = setup_driver()
    try:
        results = scrape_hacker_news(driver)
        save_results_to_csv(results)
    finally:
        driver.quit()
