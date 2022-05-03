import numpy as np
import matplotlib.pylab as plt
def step_function(x):
  return np.array(x > 0, dtype=np.int32) # xをboolean値に代え、booleanを0 or 1の数値に変換する
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.7, 1.1) # y 軸の範囲を指定
plt.show()