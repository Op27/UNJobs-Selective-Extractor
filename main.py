# Import necessary libraries for web scraping, data manipulation, and file operations
import requests  # For making HTTP requests to web pages
from bs4 import BeautifulSoup  # For parsing HTML content
import time  # For pausing the script to respect server load
import pandas as pd  # For data manipulation and export
import random  # For generating random sleep durations
import datetime  # For handling dates and times
import os  # For file operations, like opening files
import webbrowser  # For opening files in the web browser
import re  # For regular expressions, used in parsing scripts
from bs4 import NavigableString # Importing the NavigableString class from the bs4 module
import sys  # For system-specific parameters and functions

# Prompt the user for input, accepting either a country name or a full URL
user_input = input(' 🌐  Enter the country name or the full URL for job listing -> ')

# Define the base URL for UN jobs duty stations
base_site_url = "https://unjobs.org/duty_stations/"

# Determine if the user input is a URL or a country name and construct the search URL accordingly
if user_input.startswith('http://') or user_input.startswith('https://'):
    base_url = user_input
else:
    # Construct the full URL by appending the country name to the base site URL
    base_url = f"{base_site_url}{user_input.lower()}"

# Set request headers to mimic a browser user-agent for compatibility
headers = {'User-Agent': 'Mozilla/5.0'}
job_data = []  # Initialize a list to store job data
page = 1  # Start from the first page

print(' 🔍  Collecting data from the website...')

url_suffix = base_url.split('/')[-1]  # This splits the URL by '/' and takes the last element

# Loop through the pages of the website until no more job listings are found
while True:
    # Construct URL for the current page, handling the first page as a special case
    URL = f"{base_url}/{page}" if page > 1 else base_url
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract job listings from the current page
    jobs = soup.find_all('div', class_='job')
    if not jobs:
        break  # Exit the loop if no jobs are found on the current page

    # Attempt to extract script containing job closing dates
    closing_dates_script_element = soup.find("script", string=re.compile("var j\\d+i = new Date"))
    if closing_dates_script_element:
        closing_dates_script = closing_dates_script_element.string
        closing_date_matches = re.findall(r"var j(\d+)i = new Date\((\d+)\);", closing_dates_script)

        # Create a dictionary mapping from job ID suffix to closing date string
        closing_dates = {}
        for match in closing_date_matches:
            job_id_suffix, timestamp = match
            # Convert timestamp to datetime and format it
            closing_date = datetime.datetime.fromtimestamp(int(timestamp) / 1000).strftime('%Y-%m-%d')
            closing_dates[job_id_suffix] = closing_date
    else:
        closing_dates = {}   # If no closing dates script is found, use an empty dictionary

    # Iterate over each job listing to extract and store data
    for job in jobs:
        a_tag = job.find('a', class_='jtitle')
        if a_tag:
            title = a_tag.text.strip()
            url = a_tag['href']
            if a_tag.find_next('br') and a_tag.find_next('br').next_sibling:
                next_sibling = a_tag.find_next('br').next_sibling
                organization = next_sibling.strip() if isinstance(next_sibling, NavigableString) else "N/A"
            else:
                organization = "N/A" # Default to "N/A" if not found
            # Attempt to extract the organization from the job listing
            job_id_suffix = job.find("span", id=re.compile("j\d+"))['id'][1:]  
            closing_date = closing_dates.get(job_id_suffix, "N/A")
            job_data.append({'title': title, 'organization': organization, 'closing_date': closing_date, 'url': url})
     
            # Update the console with the progress
            sys.stdout.write(f'\r ⏳  Scraping information...-> {title[:50]}{" " * 10}')  # Truncate if too long and pad with spaces for clear line
            sys.stdout.flush()
    
    page += 1 # Move to the next page
    time.sleep(random.randint(2, 5))  # Pause to be respectful of the server's loadserver

sys.stdout.write('\r' + ' ' * 100 + '\r') # Clear the progress update line
sys.stdout.flush()


# Filter the collected job data for priority roles based on keywords
print(' 📊  Filtering the data based on the priority criteria...')

keywords = ['Data', 'data', 'Information', 'information', 'analysis','Analysis','Engineer','Developer','GIS','Geographic']
priority_data = [job for job in job_data if any(keyword in job['title'] for keyword in keywords)] # Adjust key words based on your needs

# Check if priority_data is empty
if not priority_data:
    priority_data = [{"title": "No positions matched with the priority criteria", "url": "", "organization": "", "closing_date": ""}]

print(' 💾  Saving data into Excel file...')

current_date = datetime.datetime.now().strftime("%Y%m%d")

# Prepare the Excel file for saving the data
df_full = pd.DataFrame(job_data)
df_priority = pd.DataFrame(priority_data)

# Dynamic filename based on the URL suffix
file_name = f"{current_date}_job_listings_{url_suffix}.xlsx"
file_path = rf'INSERT_PATH_TO_USER_FOLDER_HERE/scraping_unjobs/{file_name}'

# Save the job data to Excel with separate sheets for full and priority listings
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    df_full.to_excel(writer, index=False, sheet_name='full_list')
    df_priority.to_excel(writer, index=False, sheet_name='selected_list')

print(f" ✅  Job listings for {url_suffix.upper()} have been successfully completed!")

# Attempt to automatically open the saved Excel file
try:
    os.startfile(file_path)  # Works on Windows
except AttributeError:
    webbrowser.open(file_path)  # Cross-platform alternative