 # -*- coding: utf-8 -*- 

from visdom import Visdom
import numpy as np
import time

# 生成一个网格图
vis = Visdom(env='main')
assert vis.check_connection()

x = [0, 0, 1, 1, 0, 0, 1, 1]
y = [0, 1, 1, 0, 0, 1, 1, 0]
z = [0, 0, 0, 0, 1, 1, 1, 1]
X = np.c_[x, y, z]
print(X)
i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2]
j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3]
k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6]
Y = np.c_[i, j, k]
print(Y)

vis.mesh(X=X, Y=Y, opts=dict(opacity=0.5, color='orange'))


# 动态增加数据
# x,y=0,0
# env2 = Visdom()
# pane1= env2.line(
#     X=np.array([x]),
#     Y=np.array([y]),
#     opts=dict(title='dynamic data'))

# for i in range(10):
#     time.sleep(1) #每隔一秒钟打印一次数据
#     x+=i
#     y=(y+i)*1.5
#     print(x,y)
#     env2.line(
#         X=np.array([x]),
#         Y=np.array([y]),
#         win=pane1,#win参数确认使用哪一个pane
#         update='append') #我们做的动作是追加，除了追加意外还有其他方式，这里我们不做介绍了


# class Draw3DMesh():
#     def __init__(self, meshData):
#         # meshData shape: [x, y, z, weight, t]
#         self.meshData = meshData

#         self.vis = Visdom(env='main')
#         assert self.vis.check_connection()
