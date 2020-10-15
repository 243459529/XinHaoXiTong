import math 
import numpy as np 
import matplotlib.pyplot as plt 

def exponential_func(x, a=3): 
  y=math.pow(a, x)
  return y


X=np.linspace(-3, 3, 30) 
Y=[exponential_func(x) for x in X] 


plt.title('a^x的图像')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.plot(X, Y) 
plt.show()