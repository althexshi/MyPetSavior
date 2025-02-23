from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from backend.testAnimal import insert_pet

def clean_text(text, label):
    """Remove labels like 'Name:', 'Age:', 'Located At:' from data."""
    return text.replace(f"{label}: ", "").strip()

def scrape_24petconnect():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get("https://24petconnect.com/HaywardAdoptablePets?at=DOG")
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "gridResult"))
        )

        # Scroll to load all content
        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        animals = []
        for card in driver.find_elements(By.CLASS_NAME, "gridResult"):
            try:
                # Clean and format NAME (e.g., "ARLO (A134019)" → "ARLO")
                raw_name = clean_text(card.find_element(By.CLASS_NAME, 'line_Name').text, "Name")
                clean_name = raw_name.split('(')[0].strip()

                # Clean and format AGE (e.g., "1 Year 11 Months" → "1 year, 11 months old")
                raw_age = clean_text(card.find_element(By.CLASS_NAME, 'line_Age').text, "Age")
                formatted_age = (
                    raw_age.replace("Year", "year")
                    .replace("Month", "month")
                    .replace(" ", ", ", 1)  # Add comma after year
                    + " old"
                )

                # Clean and format BREED, GENDER, and LOCATION
                breed = clean_text(card.find_element(By.CLASS_NAME, 'line_Breed').text, "Breed")
                gender = clean_text(card.find_element(By.CLASS_NAME, 'line_Gender').text, "Gender")
                location = clean_text(card.find_element(By.CLASS_NAME, 'line_Locatedat').text, "Located At")

                # Extract image URL
                image = card.find_element(By.TAG_NAME, 'img').get_attribute('src')

                # Create animal data dictionary
                animal_data = {
                    "Name": clean_name,
                    "Age": formatted_age,
                    "Breed": breed,
                    "Gender": gender,
                    "Location": location,  # This should now be clean
                    "Image": image
                }

                # Insert into database
                insert_pet(location, None, clean_name, breed, formatted_age, None, image, gender)

                # Optional: Filter for ARLO only
                # if clean_name == "ARLO":
                animals.append(animal_data)

            except Exception as e:
                print(f"Skipping entry due to error: {e}")
                continue

        return animals

    finally:
        driver.quit()

# Run and save
data = scrape_24petconnect()
if data:
    pd.DataFrame(data).to_csv('hayward_dogs_clean.csv', index=False)
    print("Spreadsheet generated without repetitive labels!")
else:
    print("No data found")