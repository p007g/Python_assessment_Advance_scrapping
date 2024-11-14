# Python_Scrapping_and_Analysis

 Scraping and Data Analysis with Python:


## Project Overview

### Prerequisites
- Python 3.x
- Chrome browser


The assessment involves the following steps:
1. **Install all the dependencies**: Given in the [requirements.txt](requirements.txt) file

2. **Importing the required dependencies and modules**: 
```python
import pandas as pd
import numpy as np
import timeit
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
```

3. Use the timer function to calculate the total run time ---

```python
# start the timer
start_time = timeit.default_timer()

   '''-----code-----'''

# end timer
end_time = timeit.default_timer()
print(f"\nEfficient method time: {end_time - start_time}")
```

4. **Start the server**: Initialize the *Selenium Chrome Webdriver* and Automate the web browser tp open the Given URL - "https://www.barchart.com/futures".

```python
# Initialize Selenium WebDriver
driver = webdriver.Chrome()
driver.get("https://www.barchart.com/futures")

time.sleep(5)  # Allow time for the page to load
```

5. **Automate Web Scraping**: 
- Extract the "Futures Market Overview" table from the Barchart website.
- Used *try-catch block* to handle the Exception and errors.
- Used *findelement()* method of selnium webdriver to extract the text data.

```python
try:
    
    # Heading ---
    title = driver.find_element(By.CLASS_NAME, "title-wrapper").text
    print("Heading:", title)
    
    # Locate the table element ---
    element = driver.find_element(By.CLASS_NAME, "block-content")
    text_data = element.find_element(By.TAG_NAME, "div").text

except Exception as e:
    print(e)
```

6. **Data Processing**: Cleaned and Load the data into a Pandas DataFrame as per our requirements.

    ```python
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
    ```

7. **Save File**: Load and save the data in Excel file - "[Futures Market Overview_data.xlsx](https://vscode.dev/github/p007g/Python_assessment_Advance_scrapping/blob/main/Futures%20Market%20Overview_data.xlsx)"


8. #### Data Analysis:
Used Jupyter Notebook for analysis and draw the different charts - [scrape.ipynb](scrape.ipynb)

- Add a new column, "Mean," which averages "High" and "Low" prices.
- Identify the contract with the largest "Change" and retrieve its "Contract Name" and "Last" price.
- Plot the "High," "Low," and "Mean" columns on a single line chart using Matplotlib.
- Save the plot image as [High, Low, and Mean Prices by Contract.png](https://vscode.dev/github/p007g/Python_assessment_Advance_scrapping/blob/main/High%2C%20Low%2C%20and%20Mean%20Prices%20by%20Contract.png).



## Files

- **[scrape.py](scrape.py)**: Contains the Python code to perform web scraping and data processing.
- **[scrape.ipynb](scrape.ipynb)**: Contains the Python code to perform analysis and visualization.
- **[requirements.txt](requirements.txt)**: Lists all Python packages required to run the code.
- **[data/futures_data.xlsx](https://vscode.dev/github/p007g/Python_assessment_Advance_scrapping/blob/main/Futures%20Market%20Overview_data.xlsx)**: Output Excel file containing the scraped and processed data.
- **[High, Low, and Mean Prices by Contract.png](https://vscode.dev/github/p007g/Python_assessment_Advance_scrapping/blob/main/High%2C%20Low%2C%20and%20Mean%20Prices%20by%20Contract.png)**: Screenshot of the generated plot for quick reference.