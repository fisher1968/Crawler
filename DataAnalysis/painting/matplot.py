import matplotlib.pyplot as plt
from numpy.random import randn
import math
import numpy as np
from mpl_toolkits.axisartist.axislines import SubplotZero
from pylab import mpl

x = randn(50).cumsum()

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# plt.plot(x,'k--')

y = x**2

# 画一个圆
x = np.linspace(-10, 10, 500)  # 10和-10之间，均匀分布500个数字

y1 = np.sqrt(100-(x)**2)
y2 = -np.sqrt(100-(x)**2)

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)


# 在一个平面画sin，cos，tan函数

x = np.linspace(-10, 10, 500)   # 生产X坐标


# 画sin函数
y = np.sin(x)
fig = plt.figure(figsize=(10,5))
# ax = SubplotZero(fig, 1, 1, 1)
ax=fig.add_subplot(221)
plt.plot(x, y)

# 画cos函数
y=np.cos(x)

ax=fig.add_subplot(222)
ax.set_title("cos函数")
# ax.set_xticks([0,2,4,6,8,10])
# ax.set_xticklabels(["one","two","three","four","five","six"],rotation=30,fontsize="small")
# ax.axis["xzero"].set_visible(True)
# ax.axis["xzero"].label.set_text("y=0")
ax.plot(x, y)

y=np.tan(x)

fig.add_subplot(223)

plt.plot(x, y)

