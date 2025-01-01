import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = 'https://seerelvesinpokemonstyle.fandom.com'

# Read the third column from output.xlsx
df = pd.read_excel('output.xlsx', usecols=[2])

# make a list to store the skills
describe = []

# Iterate through the URLs in the specified column
for index, row in df.iterrows():
    url = row['精靈']  # Replace 'column_name' with the actual column name containing URLs
    try:
        url = url.split(' ')[1]  # Remove leading and trailing whitespace
    except IndexError:
        print(f"Invalid URL: {url}")
        describe.append('')
        continue
    full_url = URL + url  # Concatenate base URL with the URL from the column

    response = requests.get(full_url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.select_one("#mw-content-text > div > p:nth-child(6)")
    try:
        text = table.get_text(strip=True)
    except AttributeError:
        try:
            table = soup.select_one("#mw-content-text > div > p:nth-child(7)")
            text = table.get_text(strip=True)
        except AttributeError:
            try:
                table = soup.select_one("#mw-content-text > div > p:nth-child(8)")
                text = table.get_text(strip=True)
            except AttributeError:
                try:
                    table = soup.select_one("#mw-content-text > div > p:nth-child(9)")
                    text = table.get_text(strip=True)
                except AttributeError:
                    print(f"No table found at {full_url}")
                    describe.append('')
                    continue
    describe.append(text)
    print(f"Processed {full_url}")
    
# Create a new Excel writer object
df['描述'] = describe
df.to_excel('describe.xlsx', index=False)
    
    
