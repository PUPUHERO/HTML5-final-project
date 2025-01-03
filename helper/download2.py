import pandas as pd
import requests
from bs4 import BeautifulSoup

from opencc import OpenCC

converter = OpenCC('s2twp')

URL = 'https://seerelvesinpokemonstyle.fandom.com'

# Read the third column from output.xlsx
df = pd.read_excel('賽爾號精靈.xlsx', usecols=[2])

# make a list to store the skills
skills = []

# Iterate through the URLs in the specified column
for index, row in df.iterrows():
    url = row['精靈']  # Replace 'column_name' with the actual column name containing URLs
    try:
        url = url.split(' ')[1]  # Remove leading and trailing whitespace
    except IndexError:
        print(f"Invalid URL: {url}")
        df = pd.DataFrame()
        skills.append(df)
        continue
    full_url = URL + url  # Concatenate base URL with the URL from the column

    response = requests.get(full_url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", class_="sortable")
    rows = []
    try:
        for tr in table.find_all("tr"):
            row = []
            for td in tr.find_all(["td", "th"]):
                text = td.get_text(strip=True)
                row.append(text)
            rows.append(row)
    except AttributeError:
        print(f"No table found at {full_url}")
        df = pd.DataFrame()
        skills.append(df)
        continue
    df = pd.DataFrame(rows)
    
    df = df[:-1].copy()
    if len(df) > 1:
        df.columns = df.iloc[0]
        df = df[1:].reset_index(drop=True)
    
    for col in df.columns[:4]:
        df[col] = df[col].apply(lambda x: converter.convert(x))
        if col == '技能':
            df[col] = df[col].apply(lambda x: x.split('[')[0])
    
    skills.append(df)
    print(f"Processed {full_url}")
    
# Create a new Excel writer object
with pd.ExcelWriter('skills.xlsx') as writer:
    # Iterate through the list of dataframes and save each to a separate sheet
    for i, skill_df in enumerate(skills):
        skill_df.to_excel(writer, sheet_name=str(i+1), index=False)
