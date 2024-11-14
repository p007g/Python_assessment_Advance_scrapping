# --- Importing the modules ---
import pandas as pd
import numpy as np
import timeit
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# start the timer ---
start_time = timeit.default_timer()


# Initialize Selenium WebDriver ---
driver = webdriver.Chrome()
driver.get("https://www.barchart.com/futures")

time.sleep(5)  # Allow time for the page to load

try:
    
    # Heading ---
    title = driver.find_element(By.CLASS_NAME, "title-wrapper").text
    print("Title:", title)
    
    # Locate the table element
    element = driver.find_element(By.CLASS_NAME, "block-content")
    text_data = element.find_element(By.TAG_NAME, "div").text
    
    
    # Step 1: Split text by lines and clean up any extra whitespace ---
    cleaned_data = text_data.strip().splitlines()

    lines = []
    for line in cleaned_data:
        stripped_line = line.strip()  # Remove whitespace from each line
        if stripped_line:             # Only add non-empty lines
            lines.append(stripped_line)


    # Step 2: Extract headers ---
    headers = lines[:7]

    # Step 3: Process remaining lines to group them in rows ---
    data_rows = []
    for i in range(8, len(lines), 7):
        data_rows.append(lines[i:i + 7])

    # Step 4: Create a DataFrame ---
    df = pd.DataFrame(data_rows, columns=headers)

    # Display the DataFrame ---
    print(df)
    
    
except Exception as e:
    print(e)


# Save to files------
excel_file = f'Raw_Data.xlsx'
df.to_excel(excel_file, index=False)



# end timer ---
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")