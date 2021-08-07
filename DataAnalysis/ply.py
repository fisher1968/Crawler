import matplotlib.pyplot as plt
from numpy.random import randn
import math
import numpy as np
from mpl_toolkits.axisartist.axislines import SubplotZero

x = randn(50).cumsum()

# plt.plot(x,'k--')

y = x**2

# 画一个圆
x = np.linspace(-10, 10, 500)  # 10和-10之间，均匀分布500个数字

y1 = np.sqrt(100-(x)**2)
y2 = -np.sqrt(100-(x)**2)

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)


# 画sin函数

x = np.linspace(0, 10, 500)

y = np.sin(x)
fig = plt.figure()
ax = SubplotZero(fig, 1, 1, 1)
fig.add_subplot(ax)

ax.axis["xzero"].set_visible(True)
ax.axis["xzero"].label.set_text("y=0")

plt.plot(x, y)
