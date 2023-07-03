"""
1.c=point_numbers: point_numbers 是一个用于指定每个散点的颜色的列表或数组。散点图会根据 point_numbers 中的值来确定散点的颜色。
cmap=plt.cm.Blues: 指定使用蓝色调色板 (Blues) 来映射 point_numbers 中的值到颜色。不同的值会对应不同的蓝色色调。
edgecolor='none': 指定散点边界的颜色为无色，即没有边界线。

"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

#创建一个RandmWalk的实例，并将其包含的点都绘制出来
while True:
    rw = RandomWalk()
    rw.fill_walk()

    #设置绘图窗口尺寸
    plt.figure(dpi=128,figsize=(10,6))
    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values,rw.y_values,s=15,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none') #1


    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    #隐藏坐标轴
    plt.axis('off')
    
    plt.show()

    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break
