from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Define constants
CSV_FILES = ["file1.csv", "file2.csv"]  # Replace with your file names
CHROME_DRIVER_PATH = r"C:\Users\ashes\PycharmProjects\async_url_automation\chromedriver.exe"  # Replace with your ChromeDriver path
URL_COLUMN = "url"  # Replace with the column name containing the URLs in your CSV files

# Initialize the web driver
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")
options.add_argument("--mute-audio")
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=options)


# Read CSV files and extract URLs
urls = []
for csv_file in CSV_FILES:
    df = pd.read_csv(csv_file)
    urls += df[URL_COLUMN].tolist()

# Define a function to wait until the video is finished
def wait_video_completion():
    try:
        WebDriverWait(driver, 3600).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "playing-mode"))
        )
    except Exception as e:
        print(f"Error waiting for video completion: {e}")

# Open each URL, play the video, and close the tab upon completion
for url in urls:
    try:
        driver.execute_script(f"window.open('{url}', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])

        # Wait for video to start playing
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "playing-mode"))
        )

        # Wait for video to finish
        wait_video_completion()

        # Close the tab and switch back to the main window
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    except Exception as e:
        print(f"Error processing URL {url}: {e}")

# Close the browser
driver.quit()
