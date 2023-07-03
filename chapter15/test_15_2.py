"""
# 1不添加这段程序,由于数值过大,python默认由科学计数法表示,加上的这段程序后，会正常表示数值
"""

import matplotlib.pyplot as plt

x_values = list(range(1,5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,y_values,s=40)

#设置图表标题并给坐标加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Cude of Value",fontsize=14)

#设置刻度大小
plt.ticklabel_format(style='plain') # 1不添加这段程序，由于数值过大，python默认由科学计数法表示，加上的这段程序后，会正常表示数值

#颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40) 

#将图表保存
plt.savefig('Cude_plot.png', bbox_inches='tight')
