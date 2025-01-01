import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://seerelvesinpokemonstyle.fandom.com/zh/wiki/%E7%B2%BE%E7%81%B5%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9F%9F%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89?variant=zh-hant&file=%E8%B4%9D%E6%8B%89%E7%B1%B3.png"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table")
rows = []
for tr in table.find_all("tr"):
    row = []
    for td in tr.find_all(["td", "th"]):
        text = td.get_text(strip=True)
        row.append(text)
    rows.append(row)
df = pd.DataFrame(rows)
df.to_excel("output2.xlsx", index=False)