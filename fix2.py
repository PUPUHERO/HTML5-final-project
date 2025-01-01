import pandas as pd
import opencc

# 初始化 OpenCC 轉換器
converter = opencc.OpenCC('s2t')  # s2t.json 表示從簡體轉換為繁體


# Read the third column from output.xlsx
df = pd.read_excel('skills.xlsx')
