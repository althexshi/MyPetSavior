from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import re  # Import regex module
from database.insert import insert_pet  # Ensure this import matches your project structure


def clean_text(text, label):
    """
    Remove variations of the label (e.g., "Name:", "Age:", "Located At:" with any spacing or case)
    from the beginning of the text.
    """
    # Create a regex pattern that matches the label followed by optional spaces and colons
    pattern = re.compile(re.escape(label) + r'\s*[:]*\s*', re.IGNORECASE)
    return pattern.sub('', text).strip()


def scrape_24petconnect():
    # Configure headless Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    # Initialize WebDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        # Navigate to the target page
        driver.get("https://24petconnect.com/HaywardAdoptablePets?at=DOG")

        # Wait for the page to load
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

                # Debugging location
                raw_location = card.find_element(By.CLASS_NAME, 'line_Locatedat').text
                print(f"Raw Location Text: '{raw_location}'")  # Debugging
                location = clean_text(raw_location, "Located At")
                print(f"Cleaned Location: '{location}'")  # Debugging

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

                # Add to the list of animals
                # animals.append(animal_data)

            except Exception as e:
                print(f"Skipping entry due to error: {e}")
                continue

        return animals

    finally:
        # Close the browser
        driver.quit()


# Run the scraper and save results
if __name__ == "__main__":
    data = scrape_24petconnect()
    # if data:
    #     # Save to CSV
    #     pd.DataFrame(data).to_csv('hayward_dogs_clean.csv', index=False)
    #     print("Spreadsheet generated without repetitive labels!")
    # else:
    #     print("No data found")
