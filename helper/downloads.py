import pandas as pd
import requests
import os

# Load the Excel file
df = pd.read_excel('output.xlsx')

# Create a directory to save the images
if not os.path.exists('images'):
    os.makedirs('images')

# Iterate through the URLs in the specified column
for index, row in df[190:].iterrows():
    url = row['URL']  # Replace 'column_name' with the actual column name containing URLs
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'images/image_{index+1}.jpg', 'wb') as f:
                f.write(response.content)
            print(f"Downloaded image {index} from {url}")
        else:
            print(f"Failed to download image {index} from {url}")
    except Exception as e:
        print(f"Error downloading image {index} from {url}: {e}")