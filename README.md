# YouTube-Video-Automation-Script
This script allows users to automate the process of opening YouTube URLs from CSV files in a web browser, playing the videos, and closing the tabs upon video completion. The script supports processing multiple URLs from multiple CSV files.

# Requirements
Python 3.x
Google Chrome browser
ChromeDriver
Pandas library
Selenium library


# Setup
# 1. Install Python:
If you do not have Python installed on your machine, download the installer for your operating system from python.org.

# 2.Create a Virtual Environment:
It's recommended to use a virtual environment for this project to avoid potential dependency conflicts.
Navigate to your project directory and run python -m venv myenv, where myenv is the name of the virtual environment.
Activate the virtual environment using myenv\Scripts\activate on Windows or source myenv/bin/activate on Unix-like systems.

# 3.Install Required Libraries:
With the virtual environment activated, run the following commands:

 pip install pandas selenium

# Download ChromeDriver:
Visit the ChromeDriver download page and download the version that matches your Chrome browser version.
Extract the downloaded file to a location on your computer and note the path to the chromedriver executable.


# Usage


# 1. Create or Obtain CSV Files:
Prepare one or more CSV files with YouTube URLs. Ensure that each file has a column with the URLs (e.g., named "url").

# 2. Update the Script:
Open the Python script youtube_video_script.py in a text editor.
Update the CHROME_DRIVER_PATH variable with the path to the chromedriver executable.
Update the CSV_FILES variable with the paths to your CSV files.
Update the URL_COLUMN variable with the column name containing the URLs in your CSV files.

# 3.Run the Script:
Open a terminal or command prompt in your project directory.
Activate the virtual environment if it's not already active.
Run the script with the following command:

 python youtube_video_script.py

# Monitor the Progress:
The script will open a Chrome browser window, process each YouTube URL, and close the browser when finished.
Monitor the progress and check the terminal for any error messages.

# Troubleshooting
Ensure that you have the correct version of ChromeDriver that matches your Chrome browser version.
If the script does not work as expected, you may need to adjust the script or the wait conditions based on the specific YouTube video page layout or other factors.

# Note
Please use this script responsibly and in compliance with YouTube's terms of service. This script is intended for educational purposes only. It is based on the assumption that the YouTube website layout will remain the same; any changes to the layout may require script adjustments.

