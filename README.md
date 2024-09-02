# Web Automation with Selenium and Docker

## Overview

This project automates web scraping using Python and Selenium, running within a Docker environment. The script scrapes [Hacker News](https://news.ycombinator.com/) for the latest story titles and URLs, then saves the results to a CSV file.

## Project Structure

```plaintext
selenium-web-scraper/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── tests/
│       ├── __init__.py
│       └── test_selenium.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── wait-for-it.sh
Setup Instructions
Prerequisites
Docker
Docker Compose
Installation
Clone the repository:

git clone https://github.com/your-username/selenium-docker-automation.git
cd selenium-docker-automation
Build and run the Docker containers:

docker-compose up --build
The script will execute automatically, and the results will be saved to app/output/results.csv.

Running Tests
To run the tests, use:
docker-compose up test
This command will run the tests inside a Docker container using pytest.

Project Details
Scraping Target: Hacker News
Scraping Logic: Extracts the latest story titles and URLs using Selenium and saves them into a CSV file.
Tech Stack:
Python
Selenium
Docker / Docker Compose
pytest for testing
Configuration
docker-compose.yml
The docker-compose.yml defines the services needed for this project:

selenium: Runs a Selenium WebDriver (Chrome in headless mode) service.
app: Runs the Python scraping script.
test: Runs the tests for the application.
Dockerfile
Defines the environment for the Python application and installs the required dependencies.

Notes
Be sure to check the site's robots.txt file and respect the scraping guidelines of Hacker News.
The project uses a wait-for-it.sh script to ensure the Selenium WebDriver service is ready before running the Python script.
Troubleshooting
Service Not Starting: Ensure Docker is running correctly and that your machine meets the minimum system requirements.
Connection Refused: Check if the Selenium service is up by visiting http://localhost:4444/ui/.
Contributing
Feel free to fork the repository and submit a pull request with any improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Hacker News for providing the source data.
Selenium for web automation tools.
Docker for containerization.