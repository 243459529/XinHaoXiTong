import numpy as np
import matplotlib.pyplot as plt
import math

x=np.arange(-15,3*np.pi,0.01)
y=np.sin(x+math.pi)

plt.title('具有初始相位的sin(t)的图像')
plt.xlabel('                                                                          t')
plt.ylabel('x(t)=Asin(ωt+φ)')

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.plot(x,y)
plt.show()