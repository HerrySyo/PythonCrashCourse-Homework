"""
1.操作符**指数运算不支持range对象和整数之间的操作。
  确保x_value是一个包含数值的列表,而不是range对象。你可以使用list()函数将range对象转换为列表,例如x_value = list(range(10))。
2.不设置y轴坐标时y轴是以0开始的,0对应x轴的1
3.axis设置对x轴还是对y轴进行操作,which选择主刻度还是副刻度,labelsize表示刻度字体大小
"""

import matplotlib.pyplot as plt

#1 x_value = [range(1,6)]
x_value = list(range(1,6))
y_value = [x**3 for x in x_value]

plt.plot(x_value,y_value,linewidth=5)

#设置图表标题并给坐标轴加上标签
plt.title("Cube root",fontsize=20)
plt.xlabel("Value",fontsize=20)
plt.ylabel("Cube",fontsize=20)

#2 设置y轴坐标
plt.yticks([1,30,60,90,120,150])

#3 设置刻度标记大小
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()
