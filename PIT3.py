import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(-5.0,5.0,500)
plt.ylim(0,1)
f=2*np.exp((complex(-0.5,8))*-t)
plt.subplot(221)
plt.plot(t,np.real(f))


plt.title("振幅呈指数衰减的正弦信号")
plt.xlabel('t')
plt.ylabel('x(t)')

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.show()


