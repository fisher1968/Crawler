# --coding=utf-8--

import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

# pandas 显示所有行和所有列

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# 画图可以显示中文
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# df=pd.ExcelFile(r".\1.xlsx")  老的读取excel的方法
df1 = pd.read_excel(r".\1.xlsx", sheet_name='Sheet1')
# 填充所有的缺失值
df1 = df1.fillna(0)
# 按照体验分组
df2 = df1.groupby(df1['tiyan']).count()
# df2=dfdf22.fillna(0)

# df1=df1.astype("string")
df2.plot(y='name', kind='bar')

# 按照产地分组
df3 = df1.groupby(df1['from']).count()
df3 = df3.fillna(0)

df3.plot(y='name', kind='bar')
