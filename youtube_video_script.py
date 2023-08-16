from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Define constants
CSV_FILES = ["csv1.csv"]  # Replace with your file names
CHROME_DRIVER_PATH = r"C:\Users\ashes\PycharmProjects\async_url_automation\chromedriver.exe"  # Replace with your ChromeDriver path

# Initialize the web driver
from selenium.webdriver.chrome.service import Service
service = Service(executable_path=CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")
options.add_argument("--mute-audio")
driver = webdriver.Chrome(service=service, options=options)

# Read CSV files and extract URLs
urls = []
for csv_file in CSV_FILES:
    df = pd.read_csv(csv_file, header=None)
    urls += df.iloc[0].tolist()

# Open each URL in a new tab
for url in urls:
    driver.execute_script(f"window.open('{url}', '_blank');")

# Switch to each tab and play the video
for i in range(1, len(urls) + 1):
    try:
        driver.switch_to.window(driver.window_handles[i])
        time.sleep(2) # Give the page some time to load

        # Click the play button (For YouTube, the class name of the play button is 'ytp-large-play-button')
        play_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ytp-large-play-button"))
        )
        play_button.click()

    except Exception as e:
        print(f"Error processing URL {urls[i-1]}: {e}")

# Switch back to the main window if needed
driver.switch_to.window(driver.window_handles[0])

# You can close the browser after all the actions are done
# driver.quit()
