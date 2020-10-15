import math 
import numpy as np 
import matplotlib.pyplot as plt 

def exponential_func(x, a=3): 
  y=math.pow(a, x)
  return y


X=np.linspace(-3, 3, 30) 
Y1=[exponential_func(x,3) for x in X] 
Y2=[exponential_func(x,0.334) for x in X]
Y3=[exponential_func(x,1) for x in X]

plt.title('a^x的图像')
plt.xlabel('                                                                         t')
plt.ylabel('x(t)')


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.plot(X, Y1) 
plt.plot(X, Y2) 
plt.plot(X,Y3)
plt.show()