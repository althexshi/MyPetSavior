from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape_24petconnect():
    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in background
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Initialize driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get("https://24petconnect.com/HaywardAdoptablePets?at=DOG")

        # Wait for content to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "gridResult"))
        )

        # Scroll to load all results (adjust iterations as needed)
        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # Find all animal cards
        animal_cards = driver.find_elements(By.CLASS_NAME, "gridResult")
        animals = []

        for card in animal_cards:
            try:
                animal_data = {
                    'ID': card.get_attribute('id').replace('Result_', ''),
                    'Name': card.find_element(By.CLASS_NAME, 'line_Name').text,
                    'Breed': card.find_element(By.CLASS_NAME, 'line_Breed').text,
                    'Age': card.find_element(By.CLASS_NAME, 'line_Age').text,
                    'Gender': card.find_element(By.CLASS_NAME, 'line_Gender').text,
                    'Location': card.find_element(By.CLASS_NAME, 'line_Locatedat').text,
                    'Image': card.find_element(By.TAG_NAME, 'img').get_attribute('src'),
                    'URL': driver.current_url
                }
                animals.append(animal_data)
            except Exception as e:
                print(f"Error processing card: {str(e)}")
                continue

        return animals

    finally:
        driver.quit()


# Run scraper
data = scrape_24petconnect()

# Save to CSV
if data:
    df = pd.DataFrame(data)
    df.to_csv('hayward_dogs.csv', index=False)
    print(f"Successfully saved {len(data)} dogs to hayward_dogs.csv")
else:
    print("No data found")
