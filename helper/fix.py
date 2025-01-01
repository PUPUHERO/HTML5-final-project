import pandas as pd
import opencc

# 初始化 OpenCC 轉換器
converter = opencc.OpenCC('s2t')  # s2t.json 表示從簡體轉換為繁體


# Read the third column from output.xlsx
df = pd.read_excel('describe.xlsx')
df['精靈'] = df['精靈'].str.split(' ').str[0]

df2 = df.dropna(subset=['描述']).copy()
df2['描述'] = df2['描述'].apply(lambda x: converter.convert(x))

df.update(df2)

df.to_excel('describe.xlsx', index=False)