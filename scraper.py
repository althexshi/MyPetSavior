from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def selenium_scrape(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in background
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)
    time.sleep(3)  # Wait for JavaScript to load

    animals = []
    results = driver.find_elements(By.CSS_SELECTOR, 'div.gridResult')

    for result in results:
        try:
            animal_data = {
                'ID': result.get_attribute('id').replace('Result_', ''),
                'Name': result.find_element(By.CLASS_NAME, 'line_Name').text,
                'Gender': result.find_element(By.CLASS_NAME, 'line_Gender').text,
                'Breed': result.find_element(By.CLASS_NAME, 'line_Breed').text,
                'Age': result.find_element(By.CLASS_NAME, 'line_Age').text,
                'Location': result.find_element(By.CLASS_NAME, 'line_Locatedat').text,
                'Image': result.find_element(By.TAG_NAME, 'img').get_attribute('src')
            }
            animals.append(animal_data)
        except Exception as e:
            print(f"Skipping entry due to error: {str(e)}")

    driver.quit()
    return animals


# Usage
base_url = "https://www.shelterwebsite.com/dogs"
data = selenium_scrape(base_url)

# Save to CSV
if data:
    df = pd.DataFrame(data)
    df.to_csv('shelter_animals_selenium.csv', index=False)
    print(f"Saved {len(data)} animals to shelter_animals_selenium.csv")
else:
    print("No data scraped")